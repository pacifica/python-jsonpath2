#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The path module."""
from typing import Generator
from jsonpath2.node import MatchData
from jsonpath2.nodes.root import RootNode
import jsonpath2.parser as _parser


class Path:
    """
    Path parsetree object.

    The ``jsonpath2.path.Path`` class represents a JSONPath.

    .. code-block:: python

       >>> s = '{"hello":"Hello, world!"}'
       '{"hello":"Hello, world!"}'
       >>> import json
       >>> d = json.loads(s)
       {'hello':'Hello, world!'}
       >>> from jsonpath2.path import Path
       >>> p = Path.parse_str('$["hello"]')
       <jsonpath2.path.Path object>
       >>> [match_data.current_value for match_data in p.match(d)]
       ['Hello, world!']
       >>> [match_data.node.tojsonpath() for match_data in p.match(d)]
       ['$["hello"]']


    This class is constructed with respect to the given instance of the
    ``jsonpath2.nodes.root.RootNode`` class (viz., the ``root_node`` property).

    Attributes:
        - ``root_node``  The root node of the abstract syntax tree for this instance.
    """

    def __init__(self, root_node: RootNode):
        """Constructor saving the root node."""
        super(Path, self).__init__()
        if isinstance(root_node, RootNode):
            self.root_node = root_node
        else:
            raise ValueError()

    def __eq__(self, other: object) -> bool:
        """
        Check to see if two paths are the same.

        Tests if two instances are equal.
        """
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

    def __str__(self) -> str:
        """
        Stringify the path object.

        Returns the string representation of this instance.
        """
        return self.root_node.tojsonpath()

    def match(self, root_value: object) -> Generator[MatchData, None, None]:
        """
        Match root value of the path.

        Match the given JSON data structure against this instance.
        For each match, yield an instance of the ``jsonpath2.node.MatchData`` class.
        """
        return self.root_node.match(root_value, root_value)

    @classmethod
    def parse_file(cls, *args, **kwargs):
        """
        A handler to parse a file.

        Parse the contents of the given file and return a new instance of this class.
        """
        return cls(_parser.parse_file(*args, **kwargs))

    @classmethod
    def parse_str(cls, *args, **kwargs):
        """
        A handler to parse a string.

        Parse the given string and return a new instance of this class.
        """
        return cls(_parser.parse_str(*args, **kwargs))
