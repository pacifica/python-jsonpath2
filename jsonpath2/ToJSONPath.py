#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Generator

class ToJSONPath(ABC):
    def __init__(self):
        super(ToJSONPath, self).__init__()

    def tojsonpath(self) -> str:
        return ''.join(list(self.__jsonpath__()))

    @abstractmethod
    def __jsonpath__(self) -> Generator[str, None, None]:
        raise NotImplementedError()
