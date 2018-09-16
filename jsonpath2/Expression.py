#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod

from jsonpath2.ToJSONPath import ToJSONPath

class Expression(ToJSONPath):
    def __init__(self):
        super(Expression, self).__init__()

    def __eq__(self, other:object) -> bool:
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

    @abstractmethod
    def evaluate(self, root_value:object, current_value:object) -> bool:
        raise NotImplementedError()
