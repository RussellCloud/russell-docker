from Russelldocker.Service import Service

myService = Service()

print myService.list()

print myService.run('floydhub/tensorflow:latest-py2', 'floydhub', 'replicated')
