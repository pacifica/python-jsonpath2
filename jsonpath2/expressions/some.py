#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Some expression module."""
from typing import Generator
from jsonpath2.expression import Expression
from jsonpath2.node import Node


class SomeExpression(Expression):
    """The some expression class."""

    def __init__(self, next_node: Node):
        """Save the next node."""
        super(SomeExpression, self).__init__()
        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Return the next nodes jsonpath."""
        return self.next_node.__jsonpath__()

    def evaluate(self, root_value: object, current_value: object) -> bool:
        """Evaluate the next node."""
        for _next_node_match_data in self.next_node.match(root_value, current_value):
            return True
        return False
