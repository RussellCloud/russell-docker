from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='russelldocker',
    version='0.1',
    keywords=('russell', 'docker'),
    description='a library for russell docker api',
    long_description=readme(),
    license='MIT License',
    url='https://github.com/zhourunlai/russell-docker',
    author='zhourunlai',
    author_email='xiaorun95@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['docker'],
)
