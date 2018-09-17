#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Expression module."""
from abc import abstractmethod
from jsonpath2.tojsonpath import ToJSONPath


class Expression(ToJSONPath):
    """Add the expression methods to the jsonpath object."""

    def __eq__(self, other: object) -> bool:
        """Test self the same as the other object."""
        return isinstance(other, self.__class__) and (self.__dict__ == other.__dict__)

    @abstractmethod
    def evaluate(self, root_value: object, current_value: object) -> bool:  # pragma: no cover abstract method
        """Abstract method to evaluate the expression."""
        raise NotImplementedError()
