#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='api',
    version='0.1.0',
    description='Google MusicManager deduplication API',
    install_requires=[
        'requests',
    ],
    packages=find_packages()
)
