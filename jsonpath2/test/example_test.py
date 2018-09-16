#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the example module."""
from unittest import TestCase
from jsonpath2 import Example


class TestExample(TestCase):
    """Test the example class."""

    def test_add(self):
        """Test the add method in example class."""
        self.assertEqual(Example().add('123', 'abc'),
                         '123abc', 'sum of strings should work')
        self.assertEqual(Example().add(123, 456), 579,
                         'sum of integers should work')

    def test_mul(self):
        """Test the mul method in example class."""
        self.assertEqual(Example().mul('a', 4), 'aaaa',
                         'multiply of string and number should work')
        self.assertEqual(Example().mul(2, 3), 6,
                         'multiply of two integers should work')
