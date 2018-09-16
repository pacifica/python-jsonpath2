#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod
from typing import Generator

from jsonpath2.ToJSONPath import ToJSONPath

class MatchData(object):
    def __init__(self, node, root_value, current_value):
        super(MatchData, self).__init__()

        self.node = node

        self.root_value = root_value

        self.current_value = current_value

    def __eq__(self, other:object) -> bool:
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

class Node(ToJSONPath):
    def __init__(self):
        super(Node, self).__init__()

    def __eq__(self, other:object) -> bool:
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

    @abstractmethod
    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        raise NotImplementedError()
