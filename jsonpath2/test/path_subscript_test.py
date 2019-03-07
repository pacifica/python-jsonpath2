#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
from unittest import TestCase

from jsonpath2.path import Path

class TestPathSubscript(TestCase):
    """Test the path subscript."""

    def test_path_subscript_noop(self):
        """Test the path subscript with no indices."""

        s = '$["collection"][$["index"]]'
        path = Path.parse_str(s)
        self.assertEqual(s, str(path))

        data = {
            'collection': ['foo', 'bar', 'fum', 'baz'],
            'index': [],
        }

        matches = list(path.match(data))

        self.assertEqual(0, len(matches))

    def test_path_subscript_array_index(self):
        """Test the path subscript with one array index."""

        s = '$["collection"][$["index"]]'
        path = Path.parse_str(s)
        self.assertEqual(s, str(path))

        data = {
            'collection': ['foo', 'bar', 'fum', 'baz'],
            'index': 1,
        }

        matches = list(path.match(data))

        self.assertEqual(1, len(matches))
        self.assertEqual('bar', matches[0].current_value)

    def test_path_subscript_array_indices(self):
        """Test the path subscript with many array indices."""

        s = '$["collection"][$["indices"][*]]'
        path = Path.parse_str(s)
        self.assertEqual(s, str(path))

        data = {
            'collection': ['foo', 'bar', 'fum', 'baz'],
            'indices': [1, 3],
        }

        matches = list(path.match(data))

        self.assertEqual(2, len(matches))
        self.assertEqual('bar', matches[0].current_value)
        self.assertEqual('baz', matches[1].current_value)

    def test_path_subscript_object_index(self):
        """Test the path subscript with one object index."""

        s = '$["collection"][$["index"]]'
        path = Path.parse_str(s)
        self.assertEqual(s, str(path))

        data = {
            'collection': {
                'foo': 'bar',
                'fum': 'baz',
            },
            'index': 'foo',
        }

        matches = list(path.match(data))

        self.assertEqual(1, len(matches))
        self.assertEqual('bar', matches[0].current_value)

    def test_path_subscript_object_indices(self):
        """Test the path subscript with many object indices."""

        s = '$["collection"][$["indices"][*]]'
        path = Path.parse_str(s)
        self.assertEqual(s, str(path))

        data = {
            'collection': {
                'foo': 'bar',
                'fum': 'baz',
            },
            'indices': ['foo', 'fum'],
        }

        matches = list(path.match(data))

        self.assertEqual(2, len(matches))
        self.assertEqual('bar', matches[0].current_value)
        self.assertEqual('baz', matches[1].current_value)
