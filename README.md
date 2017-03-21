# russell-docker

russell-master
russell-slave1
russell-slave2
russell-slave3

## 安装 docker
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

russell-master 上运行
```
docker swarm init --advertise-addr <ip>
```

各 russell-slave 上运行
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
```
docker service create --replicas 4 --name helloworld alpine ping docker.com

docker service ps helloworld

docker service rm helloworld
```



