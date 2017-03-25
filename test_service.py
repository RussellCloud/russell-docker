from Russelldocker import Service

myService = Service()

# print myService.list()

# service = myService.get('kbtvses1f6ucok7j16v0mzo86')

# service = myService.create(image='floydhub/tensorflow:latest-py2',
#                            name='floydhub',
#                            source='/root/tensorflow-examples/3_NeuralNetworks',
#                            target='/code',
#                            constraints=['node.hostname==russell-master'],
#                            command='',
#                            workdir='/code',
#                            run_mode='jupyter')
# service = myService.create(image='floydhub/tensorflow:latest-py2',
#                            name='floydhub',
#                            source='/root/tensorflow-examples/3_NeuralNetworks',
#                            target='/code',
#                            command='python /code/dynamic_rnn.py',
#                            run_mode='cli')
service = myService.create(image='floydhub/tensorflow:latest-py3',
                           name='w821881341/rnn:52',
                           source='/root/code/9bef47551eb3422d907d324387c13ee6',
                           target='/code',
                           command='python dynamic_rnn.py',
                           workdir='/code',
                           run_mode='cli')

# print myService.get_stats('kbtvses1f6ucok7j16v0mzo86')

# log_gen = myService.get_logs('kbtvses1f6ucok7j16v0mzo86')
# print log_gen.next()
# log = list(log_gen)
# for l in log:
#     print l
