#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Wild cart subscript module."""
import itertools
from typing import Generator
from jsonpath2.node import MatchData
from jsonpath2.subscript import Subscript
from jsonpath2.subscripts.arrayindex import ArrayIndexSubscript
from jsonpath2.subscripts.objectindex import ObjectIndexSubscript


class WildcardSubscript(Subscript):
    """Wild card subscript part of the parse tree."""

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Yield the '*' wild card character."""
        yield '*'

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the root value against the current value."""
        if isinstance(current_value, dict):
            return itertools.chain(*map(
                lambda index: ObjectIndexSubscript(
                    index).match(root_value, current_value),
                current_value.keys()))
        if isinstance(current_value, list):
            return itertools.chain(*map(
                lambda index: ArrayIndexSubscript(
                    index).match(root_value, current_value),
                range(len(current_value))))
        return []
