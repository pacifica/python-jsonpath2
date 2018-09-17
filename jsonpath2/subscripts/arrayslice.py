#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Array slicing module."""
import itertools
import json
from typing import Generator
from jsonpath2.node import MatchData
from jsonpath2.subscript import Subscript
from jsonpath2.subscripts.arrayindex import ArrayIndexSubscript


class ArraySliceSubscript(Subscript):
    """Array slice class for the parse tree."""

    def __init__(self, start: int = None, end: int = None, step: int = None):
        """Save the start end and step in the array slice."""
        super(ArraySliceSubscript, self).__init__()
        self.start = start
        self.end = end
        self.step = step

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Return the jsonpath of the array slice."""
        if self.start is not None:
            yield json.dumps(self.start)
        yield ':'
        if self.end is not None:
            yield json.dumps(self.end)
        if self.step is not None:
            yield ':'
            yield json.dumps(self.step)

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match an array slice between values."""
        if isinstance(current_value, list):
            start = None if (self.start is None) else (
                self.start + (len(current_value) if (self.start < 0) else 0))

            end = None if (self.end is None) else (
                self.end + (len(current_value) if (self.end < 0) else 0))

            if start is None:
                if end is None:
                    if self.step is None:
                        indices = range(0, len(current_value))
                    else:
                        indices = range(0, len(current_value), self.step)
                else:
                    if self.step is None:
                        indices = range(0, end)
                    else:
                        indices = range(0, end, self.step)
            else:
                if end is None:
                    if self.step is None:
                        indices = range(start, len(current_value))
                    else:
                        indices = range(start, len(current_value), self.step)
                else:
                    if self.step is None:
                        indices = range(start, end)
                    else:
                        indices = range(start, end, self.step)

            return itertools.chain(*map(
                lambda index: ArrayIndexSubscript(
                    index).match(root_value, current_value),
                indices))
        return []
