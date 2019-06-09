#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The jsonpath2 module."""

from typing import Generator
from .path import Path
from .node import MatchData


def match(path_str: str, root_value: object) -> Generator[MatchData, None, None]:
    """Match root value of the path."""
    path = Path.parse_str(path_str)
    return path.match(root_value)
