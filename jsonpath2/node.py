#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The parse tree node module."""
from abc import abstractmethod
from typing import Generator
from jsonpath2.tojsonpath import ToJSONPath


# pylint: disable=too-few-public-methods
class MatchData:
    """
    Match data object for storing node values.

    The ``jsonpath2.node.MatchData`` class represents the JSON
    value and context for a JSONPath match.

    This class is constructed with respect to a root JSON value,
    a current JSON value, and an abstract syntax tree node.

    Attributes:
        - ``root_value``    The root JSON value.
        - ``current_value`` The current JSON value (i.e., the matching JSON value).
        - ``node``          The abstract syntax tree node.
    """

    def __init__(self, node, root_value, current_value):
        """Constructor to save root and current node values."""
        super(MatchData, self).__init__()
        self.node = node
        self.root_value = root_value
        self.current_value = current_value

    def __eq__(self, other: object) -> bool:
        """
        Test if two MatchData objects are the same.

        Tests if two instances are equal.
        """
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)
# pylint: enable=too-few-public-methods


class Node(ToJSONPath):
    """
    Node object for the jsonpath parsetree.

    The ``jsonpath2.node.Node`` class represents the abstract syntax tree for a JSONPath.
    """

    def __eq__(self, other: object) -> bool:
        """
        Determine if two Nodes are the same.

        Tests if two instances are equal.
        """
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

    @abstractmethod
    def match(
            self,
            root_value: object,
            current_value: object) -> Generator[MatchData, None, None]:  # pragma: no cover abstract method.
        """
        Abstract method to determine a node match.

        Match the given root and current JSON data structures against this instance.
        For each match, yield an instance of the ``jsonpath2.node.MatchData`` class.
        """
        raise NotImplementedError()
