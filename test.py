# -*- coding: utf-8 -*-

import docker

# 创建实例
client = docker.from_env()
# client = docker.DockerClient(base_url='unix://var/run/docker.sock')
# client = docker.DockerClient(base_url='tcp://127.0.0.1:1234')

# 容器列表
print client.containers.list()

# 运行容器
container = client.containers.run("alpine", ["echo", "hello", "world"], detach=True)

print container.id
print container.attrs['Config']['Image']
for line in container.logs(stream=True):
    print line.strip()

container.stop()
