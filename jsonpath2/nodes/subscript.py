#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The subscript module."""
from typing import Generator, List
from jsonpath2.node import MatchData, Node
from jsonpath2.subscript import Subscript
from jsonpath2.nodes.terminal import TerminalNode


class SubscriptNode(Node):
    """The subscript node class to handle '[]'."""

    def __init__(self, next_node: Node, subscripts: List[Subscript] = None):
        """Save the next node and subscripts."""
        super(SubscriptNode, self).__init__()
        self.next_node = next_node
        self.subscripts = subscripts if subscripts else []

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Yield the subscript characters and subscript classes."""
        yield '['
        for subscript_index, subscript in enumerate(self.subscripts):
            if subscript_index > 0:
                yield ','
            for subscript_token in subscript.__jsonpath__():
                yield subscript_token
        yield ']'
        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match root value and current value for subscripts."""
        for subscript in self.subscripts:
            for subscript_match_data in subscript.match(root_value, current_value):
                for next_node_match_data in self.next_node.match(
                        subscript_match_data.root_value, subscript_match_data.current_value):
                    if isinstance(subscript_match_data.node, TerminalNode):
                        yield next_node_match_data
                    elif isinstance(subscript_match_data.node, SubscriptNode):
                        if isinstance(subscript_match_data.node.next_node, TerminalNode):
                            yield MatchData(
                                SubscriptNode(
                                    next_node_match_data.node, subscript_match_data.node.subscripts),
                                next_node_match_data.root_value, next_node_match_data.current_value
                            )
                        else:
                            raise ValueError()
                    else:
                        raise ValueError()
