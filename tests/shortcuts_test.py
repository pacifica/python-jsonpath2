#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test package level shortcuts."""

from unittest import TestCase
import jsonpath2


class TestShortcuts(TestCase):
    """Test package level shortcuts."""

    def test_match(self):
        """Test match shortcut works."""
        data = {"hello": "Hello, World!"}
        self.assertEqual(
            [x.current_value for x in jsonpath2.match("$.hello", data)],
            ["Hello, World!"],
        )
