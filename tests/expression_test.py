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
                '$[?(@.hello >= "string")]',
                '$[?(@.hello = {"bar": "baz"})]',
                '$[?(@.hello = ["bar", "baz"])]',
                '$[?(@.hello = 42)]',
                '$[?(@.hello = 3.14159)]',
                '$[?(@.hello = false)]',
                '$[?(@.hello = true)]',
                '$[?(@.hello = null)]'
        ]:
            print(path)
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

    def test_binary_operator(self):
        """Test a binary operator."""
        expr = Path.parse_str('$[?(@ and (@ and @))]')
        self.assertEqual('$[?(@ and @ and @)]', str(expr))
        expr = Path.parse_str('$[?(@ or (@ or @))]')
        self.assertEqual('$[?(@ or @ or @)]', str(expr))
        expr = Path.parse_str('$[?(not not @)]')
        self.assertEqual('$[?(@)]', str(expr))
        expr = Path.parse_str('$[?($ = null)]')
        self.assertEqual('$[?($ = null)]', str(expr))
        with self.assertRaises(ValueError):
            Path.parse_str('$[3.14156:]')

    # pylint: disable=invalid-name
    def test_binary_operator_with_path_subscript(self):
        """Test a binary operator with a path subscript."""
        data = {
            'foo': 'bar',
            'fum': 'baz',
        }
        expected_values = {
            '$[?(0)]["foo"]': [],
            '$[?(0 = 0)]["foo"]': ['bar'],
            '$[?(0 = @["fum"])]["foo"]': [],
            '$[?(@["foo"] = 0)]["foo"]': [],
            '$[?(@["foo"] = @["fum"])]["foo"]': []
        }
        # pylint: disable=consider-iterating-dictionary
        for string in expected_values.keys():
            # pylint: enable=consider-iterating-dictionary
            expr = Path.parse_str(string)
            self.assertEqual(string, str(expr))
            values = [match_data.current_value for match_data in expr.match(data)]
            self.assertListEqual(expected_values.get(string), values)
    # pylint: enable=invalid-name
