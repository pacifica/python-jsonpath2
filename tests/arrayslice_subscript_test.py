#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the arrayslice object."""
from unittest import TestCase
from jsonpath2.subscripts.arrayslice import ArraySliceSubscript


class TestArraySliceSubscript(TestCase):
    """Test the arrayslice base class."""

    def setUp(self):
        """Setup the class."""
        self.root_value = None
        self.current_value = list(range(10))

    def test_arrayslice0(self):
        """Test the arrayslice with configuration 000 (base 2)."""
        subscript = ArraySliceSubscript(None, None, None)
        self.assertEqual(':', subscript.tojsonpath())
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], list(map(
            lambda match_data: match_data.current_value, subscript.match(self.root_value, self.current_value))))

    def test_arrayslice1(self):
        """Test the arrayslice with configuration 001 (base 2)."""
        subscript = ArraySliceSubscript(None, None, 2)
        self.assertEqual('::2', subscript.tojsonpath())
        self.assertEqual([0, 2, 4, 6, 8], list(map(
            lambda match_data: match_data.current_value, subscript.match(self.root_value, self.current_value))))

    def test_arrayslice2(self):
        """Test the arrayslice with configuration 010 (base 2)."""
        subscript = ArraySliceSubscript(None, 7, None)
        self.assertEqual(':7', subscript.tojsonpath())
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(map(
            lambda match_data: match_data.current_value, subscript.match(self.root_value, self.current_value))))

    def test_arrayslice3(self):
        """Test the arrayslice with configuration 011 (base 2)."""
        subscript = ArraySliceSubscript(None, 7, 2)
        self.assertEqual(':7:2', subscript.tojsonpath())
        self.assertEqual([0, 2, 4, 6], list(map(
            lambda match_data: match_data.current_value, subscript.match(self.root_value, self.current_value))))

    def test_arrayslice4(self):
        """Test the arrayslice with configuration 100 (base 2)."""
        subscript = ArraySliceSubscript(5, None, None)
        self.assertEqual('5:', subscript.tojsonpath())
        self.assertEqual([5, 6, 7, 8, 9], list(map(
            lambda match_data: match_data.current_value, subscript.match(self.root_value, self.current_value))))

    def test_arrayslice5(self):
        """Test the arrayslice with configuration 101 (base 2)."""
        subscript = ArraySliceSubscript(5, None, 2)
        self.assertEqual('5::2', subscript.tojsonpath())
        self.assertEqual([5, 7, 9], list(map(lambda match_data: match_data.current_value,
                                             subscript.match(self.root_value, self.current_value))))

    def test_arrayslice6(self):
        """Test the arrayslice with configuration 110 (base 2)."""
        subscript = ArraySliceSubscript(5, 7, None)
        self.assertEqual('5:7', subscript.tojsonpath())
        self.assertEqual([5, 6], list(map(lambda match_data: match_data.current_value,
                                          subscript.match(self.root_value, self.current_value))))

    def test_arrayslice7(self):
        """Test the arrayslice with configuration 111 (base 2)."""
        subscript = ArraySliceSubscript(5, 7, 2)
        self.assertEqual('5:7:2', subscript.tojsonpath())
        self.assertEqual([5], list(map(lambda match_data: match_data.current_value,
                                       subscript.match(self.root_value, self.current_value))))

    def test_arrayslice_not_list(self):
        """Test the arrayslice with non-list input."""
        subscript = ArraySliceSubscript()
        root_value = None
        self.assertTrue(not isinstance(root_value, list))
        self.assertEqual([], list(subscript.match(root_value, root_value)))
