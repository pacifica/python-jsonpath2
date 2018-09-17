#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Root node type."""
from typing import Generator
from jsonpath2.node import MatchData, Node


class RootNode(Node):
    """Root node to start the process."""

    def __init__(self, next_node: Node):
        """Save the next node object."""
        super(RootNode, self).__init__()
        self.next_node = next_node

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the root value with the current value."""
        return map(
            lambda next_node_match_data: MatchData(
                RootNode(next_node_match_data.node),
                next_node_match_data.root_value,
                next_node_match_data.current_value
            ),
            self.next_node.match(root_value, root_value)
        )

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Yield the start character string and the next node."""
        yield '$'
        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token
