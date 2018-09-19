#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Terminal node object."""
from typing import Generator
from jsonpath2.node import MatchData, Node


class TerminalNode(Node):
    """Terminal node class."""

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Return the empty array not yield."""
        return []

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match a termainal node."""
        return [MatchData(self, root_value, current_value)]
