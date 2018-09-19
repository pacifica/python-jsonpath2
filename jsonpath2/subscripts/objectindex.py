#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Object index subscript module."""
import json
from typing import Generator
from jsonpath2.node import MatchData
from jsonpath2.subscript import Subscript
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.nodes.terminal import TerminalNode


class ObjectIndexSubscript(Subscript):
    """Object index subscript part of the jsonpath parse tree."""

    def __init__(self, index: str):
        """Save the string index into the json object."""
        super(ObjectIndexSubscript, self).__init__()
        self.index = index

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Yield the dumps of the index."""
        yield json.dumps(self.index)

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the current value against the root value."""
        if isinstance(current_value, dict) and (self.index in current_value):
            return [MatchData(SubscriptNode(TerminalNode(), [self]), root_value, current_value[self.index])]
        return []
