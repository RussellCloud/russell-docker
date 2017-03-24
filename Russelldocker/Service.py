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

    # 创建服务
    def create(self, image, name, source, target, command=None, workdir=None, run_mode='cli'):
        self.service = self.client.services. \
            create(image,
                   name=name,
                   endpoint_spec={
                       'Ports': [
                           {'Protocol': 'tcp', 'PublishedPort': 8888,
                            'TargetPort': 8888},
                       ]
                   },
                   mounts=['{}:{}'.format(source, target)],
                   command=command,
                   workdir=workdir,
                   )
        print self.service

    def run2(self):
        self.service = self.client.services.create()
        print self.service

    # 获取服务日志
    def get_logs(self, id):
        service = self.client.services.get(id)
        print service.logs
