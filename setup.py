# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import reservo
version = reservo.__version__

setup(
    name='reservo',
    version=version,
    author='',
    author_email='ro@arachia.com',
    packages=[
        'reservo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7',
    ],
    zip_safe=False,
    scripts=['reservo/manage.py'],
)
