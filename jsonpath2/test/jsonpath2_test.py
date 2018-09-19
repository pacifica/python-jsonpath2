#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the jsonpath module."""
from tempfile import NamedTemporaryFile
from unittest import TestCase
from json import loads
from jsonpath2.node import MatchData
from jsonpath2.expressions.some import SomeExpression
from jsonpath2.nodes.current import CurrentNode
from jsonpath2.nodes.recursivedescent import RecursiveDescentNode
from jsonpath2.nodes.root import RootNode
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.nodes.terminal import TerminalNode
from jsonpath2.path import Path
from jsonpath2.subscripts.arrayindex import ArrayIndexSubscript
from jsonpath2.subscripts.filter import FilterSubscript
from jsonpath2.subscripts.objectindex import ObjectIndexSubscript
from jsonpath2.subscripts.wildcard import WildcardSubscript


class TestNode(TestCase):
    """Test the node object."""

    def setUp(self):
        """Setup the class."""
        root_value = {
            'hello': 'Hello, world!',
            'languages': [
                'en-GB',
                'en-US',
            ],
        }
        current_value = root_value['hello']

        self._state = [
            {
                '__jsonpath__': '',
                'node': TerminalNode(),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '$',
                'node': RootNode(TerminalNode()),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(RootNode(TerminalNode()),
                              root_value, root_value),
                ],
            },
            {
                '__jsonpath__': '@',
                'node': CurrentNode(TerminalNode()),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(CurrentNode(TerminalNode()),
                              root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '[]',
                'node': SubscriptNode(TerminalNode(), []),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [],
            },
            {
                '__jsonpath__': '[?(@)]',
                'node': SubscriptNode(TerminalNode(), [FilterSubscript(SomeExpression(CurrentNode(TerminalNode())))]),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '[?(@),?(@)]',
                'node': SubscriptNode(
                    TerminalNode(),
                    [
                        FilterSubscript(SomeExpression(
                            CurrentNode(TerminalNode()))),
                        FilterSubscript(SomeExpression(
                            CurrentNode(TerminalNode())))
                    ]
                ),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '[*]',
                'node': SubscriptNode(TerminalNode(), [WildcardSubscript()]),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [],
            },
            {
                '__jsonpath__': '[*]',
                'node': SubscriptNode(TerminalNode(), [WildcardSubscript()]),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'languages')]), root_value, root_value['languages']),
                ],
            },
            {
                '__jsonpath__': '["languages"][*]',
                'node': SubscriptNode(
                    SubscriptNode(TerminalNode(), [WildcardSubscript()]),
                    [ObjectIndexSubscript('languages')]
                ),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(0)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][0]
                    ),
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(1)]),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][1]
                    ),
                ],
            },
            {
                '__jsonpath__': '["hello","languages"]',
                'node': SubscriptNode(
                    TerminalNode(),
                    [ObjectIndexSubscript('hello'),
                     ObjectIndexSubscript('languages')]
                ),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'languages')]), root_value, root_value['languages']),
                ],
            },
            {
                '__jsonpath__': '..',
                'node': RecursiveDescentNode(TerminalNode()),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '..',
                'node': RecursiveDescentNode(TerminalNode()),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, root_value),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'languages')]), root_value, root_value['languages']),
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(0)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][0]
                    ),
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(1)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][1]
                    ),
                ],
            },
            {
                '__jsonpath__': '..[?(@)]',
                'node': RecursiveDescentNode(
                    SubscriptNode(
                        TerminalNode(),
                        [
                            FilterSubscript(SomeExpression(
                                CurrentNode(TerminalNode())))
                        ]
                    )
                ),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, root_value),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'languages')]), root_value, root_value['languages']),
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(0)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][0]
                    ),
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(1)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][1]
                    ),
                ],
            },
            {
                '__jsonpath__': '..[*]',
                'node': RecursiveDescentNode(SubscriptNode(TerminalNode(), [WildcardSubscript()])),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'languages')]), root_value, root_value['languages']),
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(0)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][0]
                    ),
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(1)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][1]
                    ),
                ],
            },
            {
                '__jsonpath__': '..["hello"]',
                'node': RecursiveDescentNode(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')])),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript(
                        'hello')]), root_value, root_value['hello']),
                ],
            },
            {
                '__jsonpath__': '..[0]',
                'node': RecursiveDescentNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)])),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(
                        SubscriptNode(
                            SubscriptNode(
                                TerminalNode(),
                                [ArrayIndexSubscript(0)]
                            ),
                            [ObjectIndexSubscript('languages')]
                        ),
                        root_value,
                        root_value['languages'][0]
                    ),
                ],
            },
        ]

    def _assert_node_test_case(self, **kwargs):
        self.assertEqual(kwargs['__jsonpath__'], kwargs['node'].tojsonpath())

        if isinstance(kwargs['node'], RootNode):
            self.assertEqual(kwargs['node'], Path.parse_str(
                kwargs['__jsonpath__']).root_node)

            with NamedTemporaryFile() as temp_file:
                temp_file.write(bytes(kwargs['__jsonpath__'], 'utf-8'))
                temp_file.seek(0)

                self.assertEqual(kwargs['node'], Path.parse_file(
                    temp_file.name).root_node)

        else:
            with self.assertRaises(ValueError):
                Path(kwargs['node'])

            with self.assertRaises(ValueError):
                Path.parse_str('__jsonpath__')

        match_data_list = list(kwargs['node'].match(
            kwargs['root_value'], kwargs['current_value']))

        for index, value in enumerate(match_data_list):
            self.assertEqual(kwargs['match_data_list'][index], value)

        for match_data in match_data_list:
            new_match_data_list = list(match_data.node.match(
                kwargs['root_value'], kwargs['current_value']))

            self.assertEqual([match_data], new_match_data_list)

    def test_state(self):
        """Test the state."""
        for kwargs in self._state:
            self._assert_node_test_case(**kwargs)

    def test_example(self):
        """Test the example from the README.md."""
        test_string = '{"hello":"Hello, world!"}'
        test_json = loads(test_string)
        path_expr = Path.parse_str('$["hello"]')
        result = list(
            map(lambda match_data: match_data.current_value, path_expr.match(test_json)))
        self.assertEqual(result[0], 'Hello, world!')
        result = list(
            map(lambda match_data: match_data.node.tojsonpath(), path_expr.match(test_json)))
        self.assertEqual(result[0], '$["hello"]')
