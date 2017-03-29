from Russelldocker import Service

myService = Service()

# print myService.list()

# service = myService.get('kbtvses1f6ucok7j16v0mzo86')

# service = myService.create(image='floydhub/tensorflow:latest-py2',
#                            name='floydhub',
#                            source='/root/code/9bef47551eb3422d907d324387c13ee6',
#                            target='/code',
#                            constraints=['node.hostname==russell-master'],
#                            command='',
#                            workdir='/code',
#                            run_mode='jupyter')
# id = myService.create(image='floydhub/tensorflow:latest-py3',
#                       name='w821881341_rnn_test',
#                       source='/root/code/9bef47551eb3422d907d324387c13ee6',
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

# oos
# sudo apt-get update
# sudo apt-get install gdebi-core
# wget http://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/32196/cn_zh/1483608175067/ossfs_1.80.0_ubuntu16.04_amd64.deb
# sudo gdebi ossfs_1.80.0_ubuntu16.04_amd64.deb
# echo russellcloud:<id>:<sercet> > /etc/passwd-ossfs
# chmod 640 /etc/passwd-ossfs
# ossfs russellcloud /root/code -ourl=oss-cn-zhangjiakou-internal.aliyuncs.com

