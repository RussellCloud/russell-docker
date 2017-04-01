from Russelldocker import Service

myService = Service()

# print myService.list()

# service = myService.get('kbtvses1f6ucok7j16v0mzo86')

service = myService.create(image='floydhub/tensorflow:latest-py2',
                           name='floydhub',
                           source='/root/code/tensorflow-examples/3_NeuralNetworks',
                           target='/code',
                           command='jupyter notebook '
                                   '--NotebookApp.token= '
                                   '--NotebookApp.base_url=abc '
                                   '--NotebookApp.default_url=/',
                           workdir='/code',
                           run_mode='jupyter')
# id = myService.create(image='floydhub/tensorflow:latest-py3',
#                       name='w821881341_rnn_test',
#                       source='/root/code/9bef47551eb3422d907d324387c13ee6',
#                       # constraints=['node.hostname==russell-master'],
#                       target='/code',
#                       command='python dynamic_rnn.py',
#                       workdir='/code',
#                       run_mode='cli')
#
# print myService.get_stats(id)

# log_gen = myService.get_logs('uh323v6dos4i')
# print log_gen.next()
# log_list = list(log_gen)
# for log in log_list:
#     print log

# print myService.stop('3tgcf33u7pp3')
