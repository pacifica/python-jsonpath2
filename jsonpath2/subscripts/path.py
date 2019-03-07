#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Path."""
from typing import Generator
from jsonpath2.node import MatchData, Node
from jsonpath2.subscript import Subscript
from jsonpath2.subscripts.arrayindex import ArrayIndexSubscript
from jsonpath2.subscripts.objectindex import ObjectIndexSubscript


class PathSubscript(Subscript):
    """Path subscript in the parse tree."""

    def __init__(self, next_node: Node):
        """Save the filter expression."""
        super(PathSubscript, self).__init__()
        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        """generate the jsonpath for the path."""
        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the path subscript against the current value."""
        for next_node_match_data in self.next_node.match(root_value, current_value):
            if isinstance(next_node_match_data.current_value, (float, int)):
                subscript = ArrayIndexSubscript(next_node_match_data.current_value)

                for subscript_match_data in subscript.match(root_value, current_value):
                    yield subscript_match_data
            elif isinstance(next_node_match_data.current_value, str):
                subscript = ObjectIndexSubscript(next_node_match_data.current_value)

                for subscript_match_data in subscript.match(root_value, current_value):
                    yield subscript_match_data
            else:
                return []
