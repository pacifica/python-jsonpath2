#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Some expression module."""
import json
from typing import Generator, Union
from jsonpath2.expression import Expression
from jsonpath2.node import Node


class SomeExpression(Expression):
    """The some expression class."""

    def __init__(self, next_node_or_value: Union[Node, object]):
        """Save the next node."""
        super(SomeExpression, self).__init__()
        self.next_node_or_value = next_node_or_value

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Return the next nodes jsonpath."""
        if isinstance(self.next_node_or_value, Node):
            return self.next_node_or_value.__jsonpath__()
        return [json.dumps(self.next_node_or_value)]

    def evaluate(self, root_value: object, current_value: object) -> bool:
        """Evaluate the next node."""
        if isinstance(self.next_node_or_value, Node):
            for _next_node_match_data in self.next_node_or_value.match(root_value, current_value):
                return True
            return False
        return bool(self.next_node_or_value)
