#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Recursive descent module."""
import itertools
from typing import Generator
from jsonpath2.node import MatchData, Node
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.subscripts.wildcard import WildcardSubscript


class RecursiveDescentNode(Node):
    """Recursive descent node class."""

    def __init__(self, next_node: Node):
        """Save the next node."""
        super(RecursiveDescentNode, self).__init__()
        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Dump the string for the previous node."""
        yield '..'
        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the root value with the current value."""
        # NOTE Depth-first
        return itertools.chain(
            self.next_node.match(root_value, current_value),
            SubscriptNode(self, [WildcardSubscript()]).match(
                root_value, current_value)
        )
