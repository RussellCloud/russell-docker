from Russelldocker import Service

myService = Service()

print myService.list()

print myService.run('floydhub/tensorflow:latest-py2', 'floydhub')

print myService.get_logs()
