#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The current node module."""
from typing import Generator
from jsonpath2.node import MatchData, Node


class CurrentNode(Node):
    """Current node class to store current node info."""

    def __init__(self, next_node: Node):
        """Save the current node."""
        super(CurrentNode, self).__init__()
        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Return the current node string."""
        yield '@'
        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the current value and root value."""
        return map(
            lambda next_node_match_data: MatchData(
                CurrentNode(next_node_match_data.node),
                next_node_match_data.root_value,
                next_node_match_data.current_value
            ),
            self.next_node.match(root_value, current_value)
        )
