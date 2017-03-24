from Russelldocker import Service

myService = Service()

# print myService.list()

# service = myService.get('h2mo8de6fj')
service = myService.create(image='floydhub/tensorflow:latest-py2',
                           name='floydhub',
                           hostname='russell-master',
                           source='/root/tensorflow-examples/3_NeuralNetworks',
                           target='/code',
                           command=['jupyter notebook'],
                           workdir='/code',
                           run_mode='jupyter')
# service = myService.create(image='floydhub/tensorflow:latest-py2',
#                            name='floydhub',
#                            source='/root/tensorflow-examples/3_NeuralNetworks',
#                            target='/code',
#                            command='python /code/dynamic_rnn.py',
#                            run_mode='cli')

# print myService.get_logs('h2mo8de6fj')
