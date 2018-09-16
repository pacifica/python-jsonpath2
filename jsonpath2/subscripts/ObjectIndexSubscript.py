#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from typing import Generator

from jsonpath2.Node import MatchData
from jsonpath2.Subscript import Subscript

from jsonpath2.nodes.SubscriptNode import SubscriptNode
from jsonpath2.nodes.TerminalNode import TerminalNode

class ObjectIndexSubscript(Subscript):
    def __init__(self, index:str):
        super(ObjectIndexSubscript, self).__init__()

        self.index = index

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield json.dumps(self.index)

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        if isinstance(current_value, dict) and (self.index in current_value):
            return [MatchData(SubscriptNode(TerminalNode(), [self]), root_value, current_value[self.index])]
        else:
            return []
