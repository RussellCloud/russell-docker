from Russelldocker import Service

myService = Service()

print myService.list()

print myService.run('floydhub/tensorflow:latest-py2', ['--name floydhub', '--mode replicated', '-p 8888:8888'])
