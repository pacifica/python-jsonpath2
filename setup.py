#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Setup and install JSONPath2 library."""
try:  # pip version 9
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements('requirements.txt', session='hack')

setup(
    name='jsonpath2',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    license='LGPLv3',
    url='https://pypi.python.org/pypi/jsonpath2/',
    description='JSONPath Parser',
    author='David Brown',
    author_email='dmlb2000@gmail.com',
    packages=find_packages(),
    install_requires=[str(ir.req) for ir in INSTALL_REQS]
)
