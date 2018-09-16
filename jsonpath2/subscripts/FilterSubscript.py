#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Generator

from jsonpath2.Expression import Expression
from jsonpath2.Node import MatchData
from jsonpath2.Subscript import Subscript

from jsonpath2.nodes.TerminalNode import TerminalNode

class FilterSubscript(Subscript):
    def __init__(self, expression:Expression):
        super(FilterSubscript, self).__init__()

        self.expression = expression

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield '?'
        yield '('

        for expression_token in self.expression.__jsonpath__():
            yield expression_token

        yield ')'

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        if self.expression.evaluate(root_value, current_value):
            return [MatchData(TerminalNode(), root_value, current_value)]
        else:
            return []
