#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Filter parse tree."""
from typing import Generator
from jsonpath2.expression import Expression
from jsonpath2.node import MatchData
from jsonpath2.subscript import Subscript
from jsonpath2.nodes.terminal import TerminalNode


class FilterSubscript(Subscript):
    """Filter subscript in the parse tree."""

    def __init__(self, expression: Expression):
        """Save the filter expression."""
        super(FilterSubscript, self).__init__()
        self.expression = expression

    def __jsonpath__(self) -> Generator[str, None, None]:
        """generate the jsonpath for the filter."""
        yield '?'
        yield '('
        for expression_token in self.expression.__jsonpath__():
            yield expression_token
        yield ')'

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the filter subscript against the current value."""
        if self.expression.evaluate(root_value, current_value):
            return [MatchData(TerminalNode(), root_value, current_value)]
        return []
