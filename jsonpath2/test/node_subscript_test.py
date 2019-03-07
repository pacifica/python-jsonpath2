#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
from unittest import TestCase

from jsonpath2.path import Path


class TestNodeSubscript(TestCase):
    """Test the node subscript."""

    # pylint: disable=invalid-name
    def test_node_subscript_noop(self):
        """Test the node subscript with no indices."""
        string = '$["collection"][$["index"]]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'collection': ['foo', 'bar', 'fum', 'baz'],
            'index': [],
        }
        matches = list(path.match(data))
        self.assertEqual(0, len(matches))
    # pylint: enable=invalid-name

    # pylint: disable=invalid-name
    def test_node_subscript_array_index(self):
        """Test the node subscript with one array index."""
        string = '$["collection"][$["index"]]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'collection': ['foo', 'bar', 'fum', 'baz'],
            'index': 1,
        }
        matches = list(path.match(data))
        self.assertEqual(1, len(matches))
        self.assertEqual('bar', matches[0].current_value)
    # pylint: enable=invalid-name

    # pylint: disable=invalid-name
    def test_node_subscript_array_indices(self):
        """Test the node subscript with many array indices."""
        string = '$["collection"][$["indices"][*]]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'collection': ['foo', 'bar', 'fum', 'baz'],
            'indices': [1, 3],
        }
        matches = list(path.match(data))
        self.assertEqual(2, len(matches))
        self.assertEqual('bar', matches[0].current_value)
        self.assertEqual('baz', matches[1].current_value)
    # pylint: enable=invalid-name

    # pylint: disable=invalid-name
    def test_node_subscript_object_index(self):
        """Test the node subscript with one object index."""
        string = '$["collection"][$["index"]]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
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
    # pylint: enable=invalid-name

    # pylint: disable=invalid-name
    def test_node_subscript_object_indices(self):
        """Test the node subscript with many object indices."""
        string = '$["collection"][$["indices"][*]]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
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
    # pylint: enable=invalid-name
