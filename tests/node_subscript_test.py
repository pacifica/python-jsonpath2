#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
from unittest import TestCase

from jsonpath2.path import Path


class TestNodeSubscript(TestCase):
    """Test the node subscript."""

    # pylint: disable=invalid-name
    def test_node_subscript(self):
        """Test the node subscript."""
        cases = [
            ([
                'foo',
                'bar',
                'fum',
                'baz',
            ], {
                '$["collection"][$["index"]]': [
                    {
                        'index': [],
                        'expected_values': [],
                    },
                    {
                        'index': 1,
                        'expected_values': ['bar'],
                    },
                ],
                '$["collection"][$["index"][*]]': [
                    {
                        'index': [1, 3],
                        'expected_values': ['bar', 'baz'],
                    },
                ],
            }),
            ({
                'foo': 'bar',
                'fum': 'baz',
            }, {
                '$["collection"][$["index"]]': [
                    {
                        'index': [],
                        'expected_values': [],
                    },
                    {
                        'index': 'foo',
                        'expected_values': ['bar'],
                    },
                ],
                '$["collection"][$["index"][*]]': [
                    {
                        'index': ['foo', 'fum'],
                        'expected_values': ['bar', 'baz'],
                    },
                ],
            }),
        ]
        for collection, cases_for_collection in cases:
            for string, cases_for_string in cases_for_collection.items():
                for case_for_string in cases_for_string:
                    path = Path.parse_str(string)
                    self.assertEqual(string, str(path))
                    matches = list(path.match({
                        'collection': collection,
                        'index': case_for_string['index'],
                    }))
                    self.assertListEqual(case_for_string['expected_values'], list(
                        map(lambda match_data: match_data.current_value, matches)))
    # pylint: enable=invalid-name
