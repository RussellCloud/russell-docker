# russell-docker

russell-master
russell-slave1
russell-slave2
russell-slave3

## 安装
```
curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
```


## 阿里云镜像加速
```
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://gz6dfepx.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload

sudo systemctl restart docker
```


## 配置 swarm 集群

主 russell-master 作为 Manager
```
docker swarm init --advertise-addr <ip>
```

各 russell-slave 作为 Worker
```
docker swarm join \
    --token <token> \
    <ip>:2377
```

查看各节点信息
```
docker node ls
```


## 部署服务

> mode=replicated|global
> replicated 意味着这个服务可以随意 scale, 自动安排这些容器运行在哪台机器上
> global 声明一个全局的服务, 在每台服务器一个容器

```
docker service create --replicas 4 --name helloworld alpine ping docker.com

docker service ps helloworld

docker service rm helloworld
```

***服务由多个任务实例组成，每个任务会启动一个容器***


## 监控

cAdvisor + InfluxDB + Grafana

```
docker network create --driver overlay logging

docker service create --network logging \
-p 8083:8083 -p 8086:8086 \
--mount source=influxdb-vol,type=volume,target=/var/lib/influxdb \
--name=influxdb --constraint 'node.hostname==russell-master' \
tutum/influxdb

docker service create --network logging \
--name cadvisor \
-p 8080:8080 \
--mode global \
--mount source=/var/run,type=bind,target=/var/run,readonly=false \
--mount source=/,type=bind,target=/rootfs,readonly=true \
--mount source=/sys,type=bind,target=/sys,readonly=true \
--mount source=/var/lib/docker,type=bind,target=/var/lib/docker,readonly=true \
google/cadvisor -storage_driver=influxdb -storage_driver_host=influxdb:8086 -storage_driver_db=cadvisor

docker service create --network logging \
-p 3000:3000 \
--name grafana \
grafana/grafana
```

## 阅读

1. [How nodes work](https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes/)
2. [How services work](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/)


## Volume 数据卷
> Docker的特性，决定了容器本身是非持久化的，容器被删除后其中的数据也一并被删除了。Docker提供数据卷（Volume），通过挂载宿主机上的目录来实现持久存储。
> 但在集群环境中，宿主机上的数据卷有很大的局限性：容器在机器间迁移时，数据无法迁移；不同机器之间不能共享数据卷。
> 为了解决这些问题，阿里云容器服务提供第三方数据卷，将各种云存储包装成数据卷，可以直接挂载在容器上，并在容器重启、迁移时自动重新挂载。目前支持ossfs和云盘两种存储。

小润在开发中遇到要给每台机器都共享用户上传的文件，并把针对不同用户上传的文件分别挂载到相应的容器中去。尝试使用 ossfs 工具 让 Aliyun OSS bucket 挂载到本地文件系统中：
[https://github.com/aliyun/ossfs](https://github.com/aliyun/ossfs)

```
# 安装命令行工具
sudo apt-get update
sudo apt-get install gdebi-core
wget http://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/32196/cn_zh/1483608175067/ossfs_1.80.0_ubuntu16.04_amd64.deb
sudo gdebi ossfs_1.80.0_ubuntu16.04_amd64.deb

# 配置与挂载
echo russellcloud:LTAIpdP2r7mjUMhW:gQqrOPmvG9NLZjRMM9cWgNBGW1TPRl > /etc/passwd-ossfs
chmod 640 /etc/passwd-ossfs
ossfs russellcloud /root/code -ourl=oss-cn-zhangjiakou-internal.aliyuncs.com

# 开机自动挂载
# 方法一：
vi /etc/fstab
ossfs#russellcloud /root/code fuse _netdev,url=oss-cn-zhangjiakou-internal.aliyuncs.com,nonempty 0 0
mount -a
# 方法二：
crontab
```

## [Rancher](http://www.rancher.com/)
![rancher](https://cdn-images-1.medium.com/max/1162/1*07ajfP09fxaU63NxPVWwbA.png)

强大的可视化管理工具，由于 swarm 模式还处于 Dev 状态，遇到坑了，我提了 [ISSUE](https://github.com/rancher/rancher/issues/8304) 还没解决(哭脸)

