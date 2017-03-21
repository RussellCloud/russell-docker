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

