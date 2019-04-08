#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Subscript module."""
from typing import Generator
from jsonpath2.node import Node, MatchData


class Subscript(Node):
    """Subscript has no value beyond a node other than type."""

    def __jsonpath__(self) -> Generator[str, None, None]:  # pragma: no cover abstract method
        """Abstract method to return the jsonpath."""

    def match(
            self,
            root_value: object,
            current_value: object) -> Generator[MatchData, None, None]:  # pragma: no cover abstract method.
        """Abstract method to determine a node match."""
