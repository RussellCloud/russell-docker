from Russelldocker import Service

myService = Service()

# print myService.list()

# service = myService.get('h2mo8de6fj')
service = myService.run(image='floydhub/tensorflow:latest-py2',
                        name='floydhub',
                        source='/root/tensorflow-examples/3_NeuralNetworks',
                        mode='jupyter')

# print myService.get_logs('h2mo8de6fj')
