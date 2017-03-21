# -*- coding: utf-8 -*-

import docker

client = docker.from_env()

print client.containers.list()

container = client.containers.run("alpine", ["echo", "hello", "world"])

for line in container.logs(stream=True):
    print line.strip()

container.stop()
