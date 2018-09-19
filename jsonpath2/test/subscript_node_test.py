#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the subscript object."""
from unittest import TestCase
from jsonpath2.node import MatchData
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.nodes.terminal import TerminalNode
from jsonpath2.subscript import Subscript


class TestSubscriptNode(TestCase):
    """Test the subscript base class."""

    def test_badsubscript1(self):
        """Test subscript that does not provide terminal or other subscript."""
        class BadSubscript1(Subscript):
            """Subscript that does not provide terminal or other subscript."""

            def __jsonpath__(self):
                """Empty."""
                return []

            def match(self, root_value, current_value):
                """One."""
                yield MatchData(None, root_value, current_value)

        self.assertEqual('', BadSubscript1().tojsonpath())

        with self.assertRaises(ValueError):
            # NOTE Use 'list' to force the computation to occur, raising any exceptions.
            list(SubscriptNode(
                TerminalNode(),
                [BadSubscript1()]
            ).match(None, None))

    def test_badsubscript2(self):
        """Test subscript that provides other subscript but not subscripted-terminal."""
        class BadSubscript2(Subscript):
            """Subscript that provides other subscript but not subscripted-terminal."""

            def __jsonpath__(self):
                """Empty."""
                return []

            def match(self, root_value, current_value):
                """One."""
                yield MatchData(SubscriptNode(None), root_value, current_value)

        self.assertEqual('', BadSubscript2().tojsonpath())

        with self.assertRaises(ValueError):
            # NOTE Use 'list' to force the computation to occur, raising any exceptions.
            list(SubscriptNode(
                TerminalNode(),
                [BadSubscript2()]
            ).match(None, None))
