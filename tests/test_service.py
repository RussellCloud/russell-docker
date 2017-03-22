import Russelldocker.Service

myService = Russelldocker.Service()

print myService.list()

print myService.run('floydhub/tensorflow:latest-py2', 'floydhub', 'replicated')
