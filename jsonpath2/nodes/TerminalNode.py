#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Generator

from jsonpath2.Node import MatchData, Node

class TerminalNode(Node):
    def __init__(self):
        super(TerminalNode, self).__init__()

    def __jsonpath__(self) -> Generator[str, None, None]:
        return []

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        return [MatchData(self, root_value, current_value)]
