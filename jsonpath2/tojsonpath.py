#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A JSONPath abstract class."""
from abc import ABC, abstractmethod
from typing import Generator


class ToJSONPath(ABC):
    """Abstract class which calls internal method."""

    def tojsonpath(self) -> str:
        """Get the json path from self and return it."""
        return ''.join(list(self.__jsonpath__()))

    @abstractmethod
    def __jsonpath__(self) -> Generator[str, None, None]:  # pragma: no cover abstract method
        """Abstract method to return the jsonpath."""
        raise NotImplementedError()
