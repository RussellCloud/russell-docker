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

# print myService.get_stats('kbtvses1f6ucok7j16v0mzo86')

log_gen = myService.get_logs('kbtvses1f6ucok7j16v0mzo86')
log = list(log_gen)
for l in log:
    print l
