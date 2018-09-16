#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Generator

from jsonpath2.Expression import Expression
from jsonpath2.Node import Node

class SomeExpression(Expression):
    def __init__(self, next_node:Node):
        super(SomeExpression, self).__init__()

        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        return self.next_node.__jsonpath__()

    def evaluate(self, root_value:object, current_value:object) -> bool:
        for next_node_match_data in self.next_node.match(root_value, current_value):
            return True

        return False
