import os
from Russelldocker import Service

myService = Service()

print myService.list()

os.system('docker service create --name floydhub --publish 8888:8888 floydhub/tensorflow:latest-py2')
