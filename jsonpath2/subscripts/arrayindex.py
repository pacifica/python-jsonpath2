#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Array Index subscript of the parse tree."""
import json
from typing import Generator
from jsonpath2.node import MatchData
from jsonpath2.subscript import Subscript
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.nodes.terminal import TerminalNode


class ArrayIndexSubscript(Subscript):
    """Array index subscript object."""

    def __init__(self, index: int):
        """Save the index of the subscript."""
        super(ArrayIndexSubscript, self).__init__()
        self.index = index

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Dump the json index when rendering jsonpath."""
        yield json.dumps(self.index)

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the root value against the current value."""
        if isinstance(current_value, list):
            if self.index < 0:
                new_index = self.index + len(current_value)

                if 0 <= new_index < len(current_value):
                    return [MatchData(SubscriptNode(TerminalNode(), [self]), root_value, current_value[new_index])]
            elif self.index < len(current_value):
                return [MatchData(SubscriptNode(TerminalNode(), [self]), root_value, current_value[self.index])]
        return []
