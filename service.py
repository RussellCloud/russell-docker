# -*- coding: utf-8 -*-

import docker

# 创建实例
client = docker.from_env()

# 服务列表
print client.services.list()

# 运行服务
service = client.services.create('floydhub/tensorflow:latest-py2', name='floydhub')

print service.id



