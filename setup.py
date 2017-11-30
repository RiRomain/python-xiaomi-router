from setuptools import setup

setup(
    name='xiaomi-router',
    version='1.0.0',
    description='Deliver info from Xiaomi Router products.',
    url='https://github.com/RiRomain/python-xiaomi-router/',
    license='MIT',
    author='RiTomain',
    author_email='romain.rinie@googlemail.com',
    packages=['xiaomirouter', 'xiaomirouter.client', 'xiaomirouter.status'],
    install_requires=['requests', ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers'
    ]
)
