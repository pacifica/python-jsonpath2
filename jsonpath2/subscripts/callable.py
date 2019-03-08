#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Callable subscript."""
import itertools
import json
from typing import Callable, Generator, Tuple, Union
from jsonpath2.node import MatchData, Node
from jsonpath2.nodes.subscript import SubscriptNode
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
            if index > 0:
                yield ','

            if isinstance(arg, Node):
                for arg_token in arg.__jsonpath__():
                    yield arg_token
            else:
                yield json.dumps(arg)

        yield ')'

    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the root value against the current value."""
        match_data_args = map(lambda arg: self._matchArgument(arg, root_value, current_value), self.args)
        for match_data_iterable in itertools.product(*match_data_args):
            args = map(lambda match_data: match_data.current_value, match_data_iterable)

            for callback_match_data in self.callback(root_value, current_value, *args):
                yield callback_match_data

    # pylint: disable=invalid-name,line-too-long,no-self-use
    def _matchArgument(self, arg: Union[Node, object], root_value: object, current_value: object) -> Generator[MatchData, None, None]:  # noqa: E501
        """Match the root value against the current value with respect to the argument."""
        if isinstance(arg, Node):
            return arg.match(root_value, current_value)
        return [MatchData(TerminalNode(), root_value, arg)]
    # pylint: enable=invalid-name,line-too-long,no-self-use


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
            yield MatchData(SubscriptNode(TerminalNode(),
                                          [ArrayLengthCallableSubscript(*args)]), root_value, len(current_value))
        elif isinstance(current_value, str):
            yield MatchData(SubscriptNode(TerminalNode(),
                                          [ArrayLengthCallableSubscript(*args)]), root_value, len(current_value))
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
            yield MatchData(SubscriptNode(TerminalNode(), [ObjectEntriesCallableSubscript(*args)]), root_value,
                            list(map(list, current_value.items())))
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
            yield MatchData(SubscriptNode(TerminalNode(), [ObjectKeysCallableSubscript(*args)]), root_value,
                            list(current_value.keys()))
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
            yield MatchData(SubscriptNode(TerminalNode(), [ObjectValuesCallableSubscript(*args)]), root_value,
                            list(current_value.values()))
    # pylint: enable=unused-argument


class StringCharAtCallableSubscript(CallableSubscript):
    """charAt(number) callable subscript object."""

    def __init__(self, *args, **kwargs):
        """Initialize the charAt(number) callable subscript object."""
        # pylint: disable=bad-continuation
        super(
            StringCharAtCallableSubscript,
            self).__init__(
            StringCharAtCallableSubscript.__match__,
            'charAt',
            *args,
            **kwargs)
        # pylint: enable=bad-continuation

    @staticmethod
    # pylint: disable=unused-argument
    def __match__(root_value: object, current_value: object, *
                  args: Tuple[object, ...]) -> Generator[object, None, None]:
        """Perform charAt(number) call."""
        if isinstance(current_value, str):
            if (len(args) == 1) and isinstance(args[0], int):
                try:
                    yield MatchData(SubscriptNode(TerminalNode(), [StringCharAtCallableSubscript(*args)]), root_value,
                                    current_value[args[0]])
                except IndexError:
                    pass
    # pylint: enable=unused-argument


class StringSubstringCallableSubscript(CallableSubscript):
    """substring(number[, number]) callable subscript object."""

    def __init__(self, *args, **kwargs):
        """Initialize the substring(number[, number]) callable subscript object."""
        # pylint: disable=bad-continuation
        super(
            StringSubstringCallableSubscript,
            self).__init__(
            StringSubstringCallableSubscript.__match__,
            'substring',
            *args,
            **kwargs)
        # pylint: enable=bad-continuation

    @staticmethod
    # pylint: disable=unused-argument
    def __match__(root_value: object, current_value: object, *
                  args: Tuple[object, ...]) -> Generator[object, None, None]:
        """Perform substring(number[, number]) call."""
        if isinstance(current_value, str):
            if (len(args) == 1) and isinstance(args[0], int):
                yield MatchData(SubscriptNode(TerminalNode(), [StringSubstringCallableSubscript(*args)]), root_value,
                                current_value[args[0]:])
            elif (len(args) == 2) and isinstance(args[0], int) and isinstance(args[1], int):
                yield MatchData(SubscriptNode(TerminalNode(), [StringSubstringCallableSubscript(*args)]), root_value,
                                current_value[args[0]:args[1]])
    # pylint: enable=unused-argument
