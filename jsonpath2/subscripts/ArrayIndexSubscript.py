#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from typing import Generator

from jsonpath2.Node import MatchData
from jsonpath2.Subscript import Subscript

from jsonpath2.nodes.SubscriptNode import SubscriptNode
from jsonpath2.nodes.TerminalNode import TerminalNode

class ArrayIndexSubscript(Subscript):
    def __init__(self, index:int):
        super(ArrayIndexSubscript, self).__init__()

        self.index = index

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield json.dumps(self.index)

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        if isinstance(current_value, list):
            if self.index < 0:
                new_index = self.index + len(current_value)

                if (new_index >= 0) and (new_index < len(current_value)):
                    return [MatchData(SubscriptNode(TerminalNode(), [self]), root_value, current_value[new_index])]
                else:
                    return []
            elif self.index < len(current_value):
                return [MatchData(SubscriptNode(TerminalNode(), [self]), root_value, current_value[self.index])]
            else:
                return []
        else:
            return []
