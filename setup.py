#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Setup the python package for jsonpath2."""
from os import path
from setuptools import setup, find_packages

setup(
    name="jsonpath2",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    license="LGPLv3",
    url="https://github.com/pacifica/python-jsonpath2/",
    description="JSONPath implementation for Python",
    long_description=open(
        path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8"
    ).read(),
    long_description_content_type="text/markdown",
    author="Mark Borkum",
    author_email="mark.borkum@pnnl.gov",
    packages=find_packages(),
    install_requires=["antlr4-python3-runtime==4.10"],
)
