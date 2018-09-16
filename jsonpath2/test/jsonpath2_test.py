#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

from jsonpath2.Node import MatchData

from jsonpath2.expressions.SomeExpression import SomeExpression

from jsonpath2.nodes.CurrentNode import CurrentNode
from jsonpath2.nodes.RecursiveDescentNode import RecursiveDescentNode
from jsonpath2.nodes.RootNode import RootNode
from jsonpath2.nodes.SubscriptNode import SubscriptNode
from jsonpath2.nodes.TerminalNode import TerminalNode

from jsonpath2.subscripts.ArrayIndexSubscript import ArrayIndexSubscript
from jsonpath2.subscripts.FilterSubscript import FilterSubscript
from jsonpath2.subscripts.ObjectIndexSubscript import ObjectIndexSubscript
from jsonpath2.subscripts.WildcardSubscript import WildcardSubscript

class TestNode(TestCase):
    def setUp(self):
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
                    MatchData(RootNode(TerminalNode()), root_value, root_value),
                ],
            },
            {
                '__jsonpath__': '@',
                'node': CurrentNode(TerminalNode()),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(CurrentNode(TerminalNode()), root_value, current_value),
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
                'node': SubscriptNode(TerminalNode(), [FilterSubscript(SomeExpression(CurrentNode(TerminalNode()))), FilterSubscript(SomeExpression(CurrentNode(TerminalNode())))]),
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
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
                ],
            },
            {
                '__jsonpath__': '["languages"][*]',
                'node': SubscriptNode(SubscriptNode(TerminalNode(), [WildcardSubscript()]), [ObjectIndexSubscript('languages')]),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][0]),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(1)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][1]),
                ],
            },
            {
                '__jsonpath__': '["hello","languages"]',
                'node': SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello'), ObjectIndexSubscript('languages')]),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
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
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][0]),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(1)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][1]),
                ],
            },
            {
                '__jsonpath__': '..[?(@)]',
                'node': RecursiveDescentNode(SubscriptNode(TerminalNode(), [FilterSubscript(SomeExpression(CurrentNode(TerminalNode())))])),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, root_value),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][0]),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(1)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][1]),
                ],
            },
            {
                '__jsonpath__': '..[*]',
                'node': RecursiveDescentNode(SubscriptNode(TerminalNode(), [WildcardSubscript()])),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][0]),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(1)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][1]),
                ],
            },
            {
                '__jsonpath__': '..["hello"]',
                'node': RecursiveDescentNode(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')])),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                ],
            },
            {
                '__jsonpath__': '..[0]',
                'node': RecursiveDescentNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)])),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][0]),
                ],
            },
        ]

    def _assertNodeTestCase(self, **kwargs):
        self.assertEqual(kwargs['__jsonpath__'], kwargs['node'].tojsonpath())

        match_data_list = list(kwargs['node'].match(kwargs['root_value'], kwargs['current_value']))

        self.assertEqual(kwargs['match_data_list'], match_data_list)

        for match_data in match_data_list:
            new_match_data_list = list(match_data.node.match(kwargs['root_value'], kwargs['current_value']))

            self.assertEqual([match_data], new_match_data_list)

    def test_state(self):
        for kwargs in self._state:
            self._assertNodeTestCase(**kwargs)
