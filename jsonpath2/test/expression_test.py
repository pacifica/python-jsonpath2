#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the expression object."""
from unittest import TestCase
from jsonpath2.path import Path
from jsonpath2.expressions.operator import OperatorExpression


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
