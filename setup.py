from distutils.core import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='Leo-Core-Logging',
    version='0.1.0',
    packages=['leo.core'],
    long_description=long_description,
    url='https://github.com/Rocklviv/leo-core-logging',
    license='GNU GPLv3',
    author='Denys Chekirda aka Rocklviv',
    author_email='dchekirda@gmail.com',
    description='Logging module for applications with possibility to switch between file / stdout.'
)
