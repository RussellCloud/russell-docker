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

    # 运行服务
    def run(self, image, name, mode, arg):
        # self.service = self.client.services.create('floydhub/tensorflow:latest-py2',
        #                                            name='floydhub',
        #                                            mode='replicated')
        self.service = self.client.services.create(image,
                                                   name=name,
                                                   mode=mode,
                                                   args=arg)
        print self.service

    # 获取服务id
    def get_id(self):
        print self.service.id
