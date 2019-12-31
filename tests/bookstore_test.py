#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
from unittest import TestCase
from jsonpath2.path import Path


class TestBookStore(TestCase):
    """
    Test the bookstore from original jsonpath article.

    http://goessner.net/articles/JsonPath/
    """

    def setUp(self):
        """Setup the class."""
        self.root_value = {
            'store': {
                'book': [
                    {
                        'category': 'reference',
                        'author': 'Nigel Rees',
                        'title': 'Sayings of the Century',
                        'price': 8.95
                    },
                    {
                        'category': 'fiction',
                        'author': 'Evelyn Waugh',
                        'title': 'Sword of Honour',
                        'price': 12.99
                    },
                    {
                        'category': 'fiction',
                        'author': 'Herman Melville',
                        'title': 'Moby Dick',
                        'isbn': '0-553-21311-3',
                        'price': 8.99
                    },
                    {
                        'category': 'fiction',
                        'author': 'J. R. R. Tolkien',
                        'title': 'The Lord of the Rings',
                        'isbn': '0-395-19395-8',
                        'price': 22.99
                    }
                ],
                'bicycle': {
                    'color': 'red',
                    'price': 19.95
                }
            }
        }

    def test_bookstore_examples_1(self):
        """
        Test the bookstore example 1.

        .. code-block:: python

           >>> expr = Path.parse_str('$.store.book[*].author')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$.store.book[*].author')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        for auth in ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']:
            self.assertTrue(auth in matches)

    def test_bookstore_examples_2(self):
        """
        Test the bookstore example 2.

        .. code-block:: python

           >>> expr = Path.parse_str('$..author')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..author')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        for auth in ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']:
            self.assertTrue(auth in matches)

    def test_bookstore_examples_3(self):
        """
        Test the bookstore example 3.

        .. code-block:: python

           >>> expr = Path.parse_str('$.store.*')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$.store.*')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertTrue(isinstance(matches[0], list))
        self.assertTrue(isinstance(matches[1], dict))
        self.assertEqual(matches[0][0]['author'], 'Nigel Rees')
        self.assertEqual(matches[1]['color'], 'red')

    def test_bookstore_examples_4(self):
        """
        Test the bookstore example 4.

        .. code-block:: python

           >>> expr = Path.parse_str('$.store..price')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$.store..price')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        for price in [8.95, 12.99, 8.99, 22.99, 19.95]:
            self.assertTrue(price in matches)

    def test_bookstore_examples_5(self):
        """
        Test the bookstore example 5.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[2]')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..book[2]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertEqual(matches[0]['category'], 'fiction')
        self.assertEqual(matches[0]['author'], 'Herman Melville')
        self.assertEqual(matches[0]['title'], 'Moby Dick')
        self.assertEqual(matches[0]['isbn'], '0-553-21311-3')
        self.assertEqual(matches[0]['price'], 8.99)

    def test_bookstore_examples_6(self):
        """
        Test the bookstore example 6.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[-1:]')
           >>> expr.match(self.root_value)
           >>> expr = Path.parse_str('$..book[-1]')
           >>> expr.match(self.root_value)
           >>> expr = Path.parse_str('$..book[3:4:1]')
           >>> expr.match(self.root_value)
        """
        for path in ['$..book[-1:]', '$..book[-1]', '$..book[3:4:1]']:
            expr = Path.parse_str(path)
            self.assertEqual(Path.parse_str(str(expr)), expr)
            matches = [x.current_value for x in expr.match(self.root_value)]
            self.assertEqual(matches[0]['category'], 'fiction')
            self.assertEqual(matches[0]['author'], 'J. R. R. Tolkien')
            self.assertEqual(matches[0]['title'], 'The Lord of the Rings')
            self.assertEqual(matches[0]['isbn'], '0-395-19395-8')
            self.assertEqual(matches[0]['price'], 22.99)

    def test_bookstore_examples_7(self):
        """
        Test the bookstore example 7.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[0,1]')
           >>> expr.match(self.root_value)
           >>> expr = Path.parse_str('$..book[:2]')
           >>> expr.match(self.root_value)
           >>> expr = Path.parse_str('$..book[:2:1]')
           >>> expr.match(self.root_value)
        """
        for path in ['$..book[0,1]', '$..book[:2]', '$..book[:2:1]']:
            expr = Path.parse_str(path)
            self.assertEqual(Path.parse_str(str(expr)), expr)
            matches = [x.current_value for x in expr.match(self.root_value)]
            self.assertEqual(matches[0]['category'], 'reference')
            self.assertEqual(matches[0]['author'], 'Nigel Rees')
            self.assertEqual(matches[0]['title'], 'Sayings of the Century')
            self.assertEqual(matches[0]['price'], 8.95)
            self.assertEqual(matches[1]['category'], 'fiction')
            self.assertEqual(matches[1]['author'], 'Evelyn Waugh')
            self.assertEqual(matches[1]['title'], 'Sword of Honour')
            self.assertEqual(matches[1]['price'], 12.99)

    def test_bookstore_examples_8(self):
        """
        Test the bookstore example 8.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[*][?(@.isbn)]')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..book[*][?(@.isbn)]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertEqual(matches[0]['category'], 'fiction')
        self.assertEqual(matches[0]['author'], 'Herman Melville')
        self.assertEqual(matches[0]['title'], 'Moby Dick')
        self.assertEqual(matches[0]['isbn'], '0-553-21311-3')
        self.assertEqual(matches[0]['price'], 8.99)
        self.assertEqual(matches[1]['category'], 'fiction')
        self.assertEqual(matches[1]['author'], 'J. R. R. Tolkien')
        self.assertEqual(matches[1]['title'], 'The Lord of the Rings')
        self.assertEqual(matches[1]['isbn'], '0-395-19395-8')
        self.assertEqual(matches[1]['price'], 22.99)

    def test_bookstore_examples_9(self):
        """
        Test the bookstore example 9.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[*][?(@.price<=10)]')
           >>> expr.match(self.root_value)
           >>> expr = Path.parse_str('$..book[*][?(@.price<10)]')
           >>> expr.match(self.root_value)
        """
        for path in ['$..book[*][?(@.price<10)]', '$..book[*][?(@.price<=10)]']:
            expr = Path.parse_str(path)
            self.assertEqual(Path.parse_str(str(expr)), expr)
            matches = [x.current_value for x in expr.match(self.root_value)]
            self.assertEqual(matches[0]['category'], 'reference')
            self.assertEqual(matches[0]['author'], 'Nigel Rees')
            self.assertEqual(matches[0]['title'], 'Sayings of the Century')
            self.assertEqual(matches[0]['price'], 8.95)
            self.assertEqual(matches[1]['category'], 'fiction')
            self.assertEqual(matches[1]['author'], 'Herman Melville')
            self.assertEqual(matches[1]['title'], 'Moby Dick')
            self.assertEqual(matches[1]['isbn'], '0-553-21311-3')
            self.assertEqual(matches[1]['price'], 8.99)

    def test_bookstore_examples_10(self):
        """
        Test the bookstore example 10.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[*][?(@.author = "Nigel Rees")]')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..book[*][?(@.author = "Nigel Rees")]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertEqual(matches[0]['category'], 'reference')
        self.assertEqual(matches[0]['author'], 'Nigel Rees')
        self.assertEqual(matches[0]['title'], 'Sayings of the Century')
        self.assertEqual(matches[0]['price'], 8.95)

    def test_bookstore_examples_11(self):
        """
        Test the bookstore example 11.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[*][?(@.category != "fiction")]')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..book[*][?(@.category != "fiction")]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertEqual(matches[0]['category'], 'reference')
        self.assertEqual(matches[0]['author'], 'Nigel Rees')
        self.assertEqual(matches[0]['title'], 'Sayings of the Century')
        self.assertEqual(matches[0]['price'], 8.95)

    def test_bookstore_examples_12(self):
        """
        Test the bookstore example 12.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[*][?(@.price>=10)]')
           >>> expr.match(self.root_value)
           >>> expr = Path.parse_str('$..book[*][?(@.price>10)]')
           >>> expr.match(self.root_value)
        """
        for path in ['$..book[*][?(@.price>10)]', '$..book[*][?(@.price>=10)]']:
            expr = Path.parse_str(path)
            self.assertEqual(Path.parse_str(str(expr)), expr)
            matches = [x.current_value for x in expr.match(self.root_value)]
            self.assertEqual(matches[0]['category'], 'fiction')
            self.assertEqual(matches[0]['author'], 'Evelyn Waugh')
            self.assertEqual(matches[0]['title'], 'Sword of Honour')
            self.assertEqual(matches[0]['price'], 12.99)
            self.assertEqual(matches[1]['category'], 'fiction')
            self.assertEqual(matches[1]['author'], 'J. R. R. Tolkien')
            self.assertEqual(matches[1]['title'], 'The Lord of the Rings')
            self.assertEqual(matches[1]['isbn'], '0-395-19395-8')
            self.assertEqual(matches[1]['price'], 22.99)


class TestExtendedBookStore(TestCase):
    """This test extends the standard bookstore test for completness."""

    def setUp(self):
        """Copy the original bookstore document to this class."""
        orig_bookstore = TestBookStore()
        orig_bookstore.setUp()
        self.root_value = orig_bookstore.root_value

    def test_bookstore_extexample_1(self):
        """
        Test the bookstore example with step function.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[::2]')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..book[::2]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertEqual(matches[0]['category'], 'reference')
        self.assertEqual(matches[0]['author'], 'Nigel Rees')
        self.assertEqual(matches[0]['title'], 'Sayings of the Century')
        self.assertEqual(matches[0]['price'], 8.95)
        self.assertEqual(matches[1]['category'], 'fiction')
        self.assertEqual(matches[1]['author'], 'Herman Melville')
        self.assertEqual(matches[1]['title'], 'Moby Dick')
        self.assertEqual(matches[1]['isbn'], '0-553-21311-3')
        self.assertEqual(matches[1]['price'], 8.99)

    def test_bookstore_extexamples_2(self):
        """
        Test the bookstore example slice with end and multiple colons.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[:2:]')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..book[:2:]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertEqual(matches[0]['category'], 'reference')
        self.assertEqual(matches[0]['author'], 'Nigel Rees')
        self.assertEqual(matches[0]['title'], 'Sayings of the Century')
        self.assertEqual(matches[0]['price'], 8.95)
        self.assertEqual(matches[1]['category'], 'fiction')
        self.assertEqual(matches[1]['author'], 'Evelyn Waugh')
        self.assertEqual(matches[1]['title'], 'Sword of Honour')
        self.assertEqual(matches[1]['price'], 12.99)

    def test_bookstore_extexamples_3(self):
        """
        Test the bookstore example slice with start and multiple colons.

        .. code-block:: python

           >>> expr = Path.parse_str('$..book[2::]')
           >>> expr.match(self.root_value)
        """
        expr = Path.parse_str('$..book[2::]')
        self.assertEqual(Path.parse_str(str(expr)), expr)
        matches = [x.current_value for x in expr.match(self.root_value)]
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0]['category'], 'fiction')
        self.assertEqual(matches[0]['author'], 'Herman Melville')
        self.assertEqual(matches[0]['title'], 'Moby Dick')
        self.assertEqual(matches[0]['isbn'], '0-553-21311-3')
        self.assertEqual(matches[0]['price'], 8.99)
