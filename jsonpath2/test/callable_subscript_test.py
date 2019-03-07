#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
from unittest import TestCase
from jsonpath2.path import Path


class TestCallableSubscript(TestCase):
    """Test the callable subscript."""

    def test_length(self):
        """Test the length() callable subscript."""
        string = '$["collection"][length()]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'collection': ['foo', 'bar', 'fum', 'baz'],
        }
        matches = list(path.match(data))
        self.assertEqual(1, len(matches))
        self.assertEqual(4, matches[0].current_value)

        string = '$["scalar"][length()]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'scalar': 'Hello, world!',
        }
        matches = list(path.match(data))
        self.assertEqual(1, len(matches))
        self.assertEqual(len('Hello, world!'), matches[0].current_value)

    def test_entries(self):
        """Test the entries() callable subscript."""
        string = '$["collection"][entries()][*]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'collection': {
                'foo': 'bar',
                'fum': 'baz',
            },
        }
        matches = list(path.match(data))
        self.assertEqual(2, len(matches))
        self.assertListEqual(['foo', 'bar'], matches[0].current_value)
        self.assertListEqual(['fum', 'baz'], matches[1].current_value)

    def test_keys(self):
        """Test the keys() callable subscript."""
        string = '$["collection"][keys()][*]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'collection': {
                'foo': 'bar',
                'fum': 'baz',
            },
        }
        matches = list(path.match(data))
        self.assertEqual(2, len(matches))
        self.assertEqual('foo', matches[0].current_value)
        self.assertEqual('fum', matches[1].current_value)

    def test_values(self):
        """Test the values() callable subscript."""
        string = '$["collection"][values()][*]'
        path = Path.parse_str(string)
        self.assertEqual(string, str(path))
        data = {
            'collection': {
                'foo': 'bar',
                'fum': 'baz',
            },
        }
        matches = list(path.match(data))
        self.assertEqual(2, len(matches))
        self.assertEqual('bar', matches[0].current_value)
        self.assertEqual('baz', matches[1].current_value)
