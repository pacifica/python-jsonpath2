#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The jsonpath2 module."""

from typing import Generator
from .path import Path
from .node import MatchData


def match(path_str: str, root_value: object) -> Generator[MatchData, None, None]:
    """
    Match root value of the path.

    The ``jsonpath2.match`` function is a shortcut to match a given JSON data
    structure against a JSONPath string.

    .. code-block:: python

       >>> import jsonpath2
       >>> doc = {'hello': 'Hello, world!'}
       >>> [x.current_value for x in jsonpath2.match('$.hello', doc)]
       ['Hello, world!']
    """
    path = Path.parse_str(path_str)
    return path.match(root_value)
