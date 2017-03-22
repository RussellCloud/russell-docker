# -*- coding: utf-8 -*-

import docker
import os


class Service:
    # 创建实例
    def __init__(self):
        self.client = docker.from_env()
        # self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        # self.client = docker.DockerClient(base_url='tcp://127.0.0.1:1234')

    # 服务列表
    def list(self):
        print self.client.services.list()

    # 运行服务
    def run(self, image, name):
        print self.client.services.create(image, name=name, endpoint_config={
            'Ports': [
                {'Protocol': 'tcp', 'PublishedPort': 8888, 'TargetPort': 8888},
            ]
        })

    # 获取服务日志
    def get_logs(self):
        print self.client.service.logs()
