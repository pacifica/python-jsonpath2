#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the expression object."""
from unittest import TestCase
from jsonpath2.expressions.operator import OperatorExpression, AndVariadicOperatorExpression
from jsonpath2.expressions.some import SomeExpression
from jsonpath2.nodes.current import CurrentNode
from jsonpath2.nodes.terminal import TerminalNode
from jsonpath2.path import Path


class TestExpression(TestCase):
    """Test the expression base class."""

    def test_expression(self):
        """Test the base expression equal."""
        obj_a = OperatorExpression()
        obj_b = OperatorExpression()
        self.assertTrue(obj_a == obj_b)

    def test_failure_expressions(self):
        """Test expressions that make no sense."""
        data = {'hello': 'Hello, World!'}
        for path in [
                '$[?(@.hello < "string")]',
                '$[?(@.hello <= "string")]',
                '$[?(@.hello > "string")]',
                '$[?(@.hello >= "string")]'
        ]:
            expr = Path.parse_str(path)
            self.assertFalse([x for x in expr.match(data)])

    def test_unary_operator(self):
        """Test the unary not in a path."""
        data = [
            {
                'hello': 'Hello, World!',
                'bar': False
            }
        ]
        expr = Path.parse_str('$[?(not @.bar)]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        self.assertTrue([x for x in expr.match(data)])

    def test_unary_boolean_operator(self):
        """Test the unary not in a path."""
        data = [
            {
                'hello': 'Hello, World!',
                'bar': False
            }
        ]
        expr = Path.parse_str('$[?(not (@.bar or (@.fiz > 2 and @.biz > 2)))]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        self.assertTrue([x for x in expr.match(data)])

    def test_variadic_operator(self):
        """Test a variadic operator."""
        expr = AndVariadicOperatorExpression([])
        self.assertEqual('', expr.tojsonpath())
        expr = AndVariadicOperatorExpression(
            [SomeExpression(CurrentNode(TerminalNode()))])
        self.assertEqual('@', expr.tojsonpath())
