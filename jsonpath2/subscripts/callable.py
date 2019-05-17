#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Callable subscript."""
import itertools
import json
from typing import Generator, Tuple, Union
from jsonpath2.node import MatchData, Node
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.nodes.terminal import TerminalNode
from jsonpath2.subscript import Subscript


class CallableSubscript(Subscript):
    """Callable subscript object."""

    def __init__(self, *args: Tuple[Union[MatchData, Node, object]]):
        """Initialize the callable subscript object."""
        super(CallableSubscript, self).__init__()
        self.args = args

    def __call__(
            self,
            root_value: object,
            current_value: object) -> Generator[MatchData, None, None]:  # pragma: no cover abstract method.
        """Call the callable subscript object."""
        raise NotImplementedError()

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Generate the JSONPath for the callable subscript."""
        yield self.__class__.__str__

        yield '('

        for index, arg in enumerate(self.args):
            if index > 0:
                yield ','

            if isinstance(arg, MatchData):
                yield json.dumps(arg.current_value)
            elif isinstance(arg, Node):
                for arg_token in arg.__jsonpath__():
                    yield arg_token
            else:
                yield json.dumps(arg)

        yield ')'

    # pylint: disable=line-too-long
    def match(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Match the root value against the current value."""
        for args in itertools.product(*map(lambda arg: [arg] if isinstance(arg, MatchData) else arg.match(root_value, current_value) if isinstance(arg, Node) else [MatchData(TerminalNode(), root_value, arg)], self.args)):  # noqa: E501
            for callable_subscript_match_data in self.__class__(*args)(root_value, current_value):
                yield callable_subscript_match_data
    # pylint: enable=line-too-long


class CharAtCallableSubscript(CallableSubscript):
    """charAt(int) callable subscript object."""

    __str__ = 'charAt'

    def __call__(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Perform charAt(number) call."""
        if isinstance(current_value, str):
            if (len(self.args) == 1) \
                    and isinstance(self.args[0].current_value, int):
                try:
                    value = current_value[self.args[0].current_value]
                except IndexError:
                    pass
                else:
                    yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                    root_value, value)


class EntriesCallableSubscript(CallableSubscript):
    """entries() callable subscript object."""

    __str__ = 'entries'

    def __call__(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Perform entries() call."""
        if isinstance(current_value, dict):
            if not self.args:
                value = list(map(list, current_value.items()))

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)
        elif isinstance(current_value, list):
            if not self.args:
                value = list(map(list, enumerate(current_value)))

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)


class KeysCallableSubscript(CallableSubscript):
    """keys() callable subscript object."""

    __str__ = 'keys'

    def __call__(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Perform keys() call."""
        if isinstance(current_value, dict):
            if not self.args:
                value = list(current_value.keys())

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)
        elif isinstance(current_value, list):
            if not self.args:
                value = list(range(len(current_value)))

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)


class LengthCallableSubscript(CallableSubscript):
    """length() callable subscript object."""

    __str__ = 'length'

    def __call__(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Perform length() call."""
        if isinstance(current_value, list):
            if not self.args:
                value = len(current_value)

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)
        elif isinstance(current_value, str):
            if not self.args:
                value = len(current_value)

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)


class SubstringCallableSubscript(CallableSubscript):
    """substring(int[, int]) callable subscript object."""

    __str__ = 'substring'

    def __call__(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Perform substring(number[, number]) call."""
        if isinstance(current_value, str):
            if (len(self.args) == 1) \
                    and isinstance(self.args[0].current_value, int):
                value = current_value[self.args[0].current_value:]

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)
            elif (len(self.args) == 2) \
                    and isinstance(self.args[0].current_value, int) \
                    and isinstance(self.args[1].current_value, int):
                value = current_value[self.args[0].current_value:self.args[1].current_value]

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)


class ValuesCallableSubscript(CallableSubscript):
    """values() callable subscript object."""

    __str__ = 'values'

    def __call__(self, root_value: object, current_value: object) -> Generator[MatchData, None, None]:
        """Perform values() call."""
        if isinstance(current_value, dict):
            if not self.args:
                value = list(current_value.values())

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)
        elif isinstance(current_value, list):
            if not self.args:
                value = current_value

                yield MatchData(SubscriptNode(TerminalNode(), [self]),
                                root_value, value)
