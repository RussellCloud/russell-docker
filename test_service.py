from Russelldocker import Service

myService = Service()

# print myService.list()

# service = myService.get('h2mo8de6fj')
service = myService.create(image='floydhub/tensorflow:latest-py2',
                           name='floydhub',
                           source='/root/tensorflow-examples/3_NeuralNetworks',
                           target='/root',
                           command=['cd /root', 'jupyter notebook'],
                           run_mode='jupyter')
# service = myService.create(image='floydhub/tensorflow:latest-py2',
#                            name='floydhub',
#                            source='/root/tensorflow-examples/3_NeuralNetworks',
#                            target='/root',
#                            command='python /root/dynamic_rnn.py',
#                            run_mode='cli')

# print myService.get_logs('h2mo8de6fj')
