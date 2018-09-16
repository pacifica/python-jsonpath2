#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    description='JSONPath implementation for Python',
    author='Mark Borkum',
    author_email='mark.borkum@pnnl.gov',
    packages=find_packages(),
    namespace_packages=['jsonpath2'],
    install_requires=[str(ir.req) for ir in INSTALL_REQS]
)
