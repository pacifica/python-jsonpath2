#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Callable subscript."""
import itertools
import json
from typing import Callable, Generator, Tuple, Union
from jsonpath2.node import MatchData, Node
from jsonpath2.nodes.terminal import TerminalNode
from jsonpath2.subscript import Subscript


class CallableSubscript(Subscript):
    """Callable subscript object."""

    # pylint: disable=line-too-long
    def __init__(self, callback: Callable[[Tuple[object, ...]], Generator[object,  # noqa: E501
                                                                          None, None]], name: str, *args: Tuple[Union[Node, object]]):  # noqa: E501
        """Initialize the callable subscript object."""
        super(CallableSubscript, self).__init__()
        self.callback = callback
        self.name = name
        self.args = args
    # pylint: enable=line-too-long

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Generate the JSONPath for the callable subscript."""
        yield self.name
        yield '('

        for index, arg in enumerate(self.args):
            if index == 0:
                yield ','

            if isinstance(arg, Node):
                for arg_token in arg.__jsonpath__():
                    yield arg_token
            else:
                yield json.dumps(arg)

        yield ')'

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the root value against the current value."""
        for match_data_iterable in itertools.product(
                *map(lambda arg: arg.match(root_value, current_value) if isinstance(arg, Node) else [arg], self.args)):
            args = map(lambda match_data: match_data.current_value, match_data_iterable)

            for callback_value in self.callback(root_value, current_value, *args):
                yield MatchData(TerminalNode(), root_value, callback_value)


class ArrayLengthCallableSubscript(CallableSubscript):
    """length() callable subscript object."""

    def __init__(self, *args, **kwargs):
        """Initialize the length() callable subscript object."""
        # pylint: disable=bad-continuation
        super(
            ArrayLengthCallableSubscript,
            self).__init__(
            ArrayLengthCallableSubscript.__match__,
            'length',
            *args,
            **kwargs)
        # pylint: disable=bad-continuation

    @staticmethod
    # pylint: disable=unused-argument
    def __match__(root_value: object, current_value: object, *
                  args: Tuple[object, ...]) -> Generator[object, None, None]:
        """Perform length() call."""
        if isinstance(current_value, list):
            yield len(current_value)
        elif isinstance(current_value, str):
            yield len(current_value)
    # pylint: enable=unused-argument


class ObjectEntriesCallableSubscript(CallableSubscript):
    """entries() callable subscript object."""

    def __init__(self, *args, **kwargs):
        """Initialize the entries() callable subscript object."""
        # pylint: disable=bad-continuation
        super(
            ObjectEntriesCallableSubscript,
            self).__init__(
            ObjectEntriesCallableSubscript.__match__,
            'entries',
            *args,
            **kwargs)
        # pylint: enable=bad-continuation

    @staticmethod
    # pylint: disable=unused-argument
    def __match__(root_value: object, current_value: object, *
                  args: Tuple[object, ...]) -> Generator[object, None, None]:
        """Perform entries() call."""
        if isinstance(current_value, dict):
            yield list(map(list, current_value.items()))
    # pylint: enable=unused-argument


class ObjectKeysCallableSubscript(CallableSubscript):
    """keys() callable subscript object."""

    def __init__(self, *args, **kwargs):
        """Initialize the keys() callable subscript object."""
        # pylint: disable=bad-continuation
        super(
            ObjectKeysCallableSubscript,
            self).__init__(
            ObjectKeysCallableSubscript.__match__,
            'keys',
            *args,
            **kwargs)
        # pylint: enable=bad-continuation

    @staticmethod
    # pylint: disable=unused-argument
    def __match__(root_value: object, current_value: object, *
                  args: Tuple[object, ...]) -> Generator[object, None, None]:
        """Perform keys() call."""
        if isinstance(current_value, dict):
            yield list(current_value.keys())
    # pylint: enable=unused-argument


class ObjectValuesCallableSubscript(CallableSubscript):
    """values() callable subscript object."""

    def __init__(self, *args, **kwargs):
        """Initialize the values() callable subscript object."""
        # pylint: disable=bad-continuation
        super(
            ObjectValuesCallableSubscript,
            self).__init__(
            ObjectValuesCallableSubscript.__match__,
            'values',
            *args,
            **kwargs)
        # pylint: enable=bad-continuation

    @staticmethod
    # pylint: disable=unused-argument
    def __match__(root_value: object, current_value: object, *
                  args: Tuple[object, ...]) -> Generator[object, None, None]:
        """Perform values() call."""
        if isinstance(current_value, dict):
            yield list(current_value.values())
    # pylint: enable=unused-argument
