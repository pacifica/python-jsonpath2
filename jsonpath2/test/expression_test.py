#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the expression object."""
from unittest import TestCase
from jsonpath2.expressions.operator import OperatorExpression


class TestExpression(TestCase):
    """Test the expression base class."""

    def test_expression(self):
        """Test the base expression equal."""
        obj_a = OperatorExpression()
        obj_b = OperatorExpression()
        self.assertTrue(obj_a == obj_b)
