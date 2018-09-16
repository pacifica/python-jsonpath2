#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Generator

from jsonpath2.Node import MatchData
from jsonpath2.nodes.RootNode import RootNode
import jsonpath2.parser as _parser

class Path(object):
    def __init__(self, root_node:RootNode):
        super(Path, self).__init__()

        if isinstance(root_node, RootNode):
            self.root_node = root_node
        else:
            raise ValueError()

    def __eq__(self, other:object) -> bool:
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

    def __str__(self) -> str:
        return self.root_node.tojsonpath()

    def match(self, root_value:object) -> Generator[MatchData, None, None]:
        return self.root_node.match(root_value, root_value)

    @classmethod
    def parse_file(self, *args, **kwargs):
        return Path(_parser.parse_file(*args, **kwargs))

    @classmethod
    def parse_str(self, *args, **kwargs):
        return Path(_parser.parse_str(*args, **kwargs))
