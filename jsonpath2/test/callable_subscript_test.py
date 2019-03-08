#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
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
