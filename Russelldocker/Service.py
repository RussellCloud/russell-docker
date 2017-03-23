# -*- coding: utf-8 -*-

import docker


class Service:
    # 创建实例
    def __init__(self):
        self.client = docker.from_env()
        # self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        # self.client = docker.DockerClient(base_url='tcp://127.0.0.1:1234')
        self.service = ''

    # 服务列表
    def list(self):
        print self.client.services.list()

    # 获取服务
    def get(self, id):
        self.service = self.client.services.get(id)
        print self.service

    # 运行服务
    def run(self, image, name):
        self.service = self.client.services. \
            create(image,
                   name=name,
                   endpoint_spec={
                       'Ports': [
                           {'Protocol': 'tcp', 'PublishedPort': 8888,
                            'TargetPort': 8888},
                       ]
                   },
                   mounts=['/root/tensorflow-examples/3_NeuralNetworks:/root:ro'],
                   command='python /root/dynamic_rnn.py'
                   )
        print self.service

    # 获取服务日志
    def get_logs(self, id):
        service = self.client.services.get(id)
        print service.logs
