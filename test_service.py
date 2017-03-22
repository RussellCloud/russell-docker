from Russelldocker import Service

myService = Service()

# print myService.list()

service = myService.get('h2mo8de6fj')
# service = myService.run('floydhub/tensorflow:latest-py2', 'floydhub')

print service.logs
