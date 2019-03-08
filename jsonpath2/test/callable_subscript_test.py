#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
import re
from unittest import TestCase

from jsonpath2.path import Path


class TestCallableSubscript(TestCase):
    """Test the callable subscript."""

    # pylint: disable=invalid-name
    def test_callable_subscript(self):
        """Test the callable subscript."""
        cases = [
            ('Hello, world!', {
                '$[length()]': [len('Hello, world!')],
                '$[charAt(5)]': ['Hello, world!'[5]],
                '$[charAt($[length()])]': [],
                '$[substring(5)]': ['Hello, world!'[5:]],
                '$[substring(5,7)]': ['Hello, world!'[5:7]],
            }),
            ([
                'foo',
                'bar',
                'fum',
                'baz',
            ], {
                '$[length()]': [4],
            }),
            ({
                'foo': 'bar',
                'fum': 'baz',
            }, {
                '$[entries()][*]': [['foo', 'bar'], ['fum', 'baz']],
                '$[keys()][*]': ['foo', 'fum'],
                '$[values()][*]': ['bar', 'baz'],
            }),
        ]
        for collection, cases_for_collection in cases:
            for string, expected_values in cases_for_collection.items():
                path = Path.parse_str(string)
                self.assertEqual(string, str(path))
                matches = list(path.match(collection))
                self.assertListEqual(expected_values, list(
                    map(lambda match_data: match_data.current_value, matches)))
    # pylint: enable=invalid-name

    # pylint: disable=invalid-name
    def test_parse_callable_subscript(self):
        """Test parsing callable subscript."""
        with self.assertRaisesRegex(ValueError, r'^' + re.escape('callable subscript \'foo\' not found') + '$'):
            Path.parse_str('$.foo(1, 2, 3)')
    # pylint: enable=invalid-name
