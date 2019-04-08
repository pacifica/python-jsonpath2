#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The path module."""
from typing import Generator
from jsonpath2.node import MatchData
from jsonpath2.nodes.root import RootNode
import jsonpath2.parser as _parser


class Path:
    """Path parsetree object."""

    def __init__(self, root_node: RootNode):
        """Constructor saving the root node."""
        super(Path, self).__init__()
        if isinstance(root_node, RootNode):
            self.root_node = root_node
        else:
            raise ValueError()

    def __eq__(self, other: object) -> bool:
        """Check to see if two paths are the same."""
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

    def __str__(self) -> str:
        """Stringify the path object."""
        return self.root_node.tojsonpath()

    def match(self, root_value: object) -> Generator[MatchData, None, None]:
        """Match root value of the path."""
        return self.root_node.match(root_value, root_value)

    @classmethod
    def parse_file(cls, *args, **kwargs):
        """A handler to parse a file."""
        return cls(_parser.parse_file(*args, **kwargs))

    @classmethod
    def parse_str(cls, *args, **kwargs):
        """A handler to parse a string."""
        return cls(_parser.parse_str(*args, **kwargs))
