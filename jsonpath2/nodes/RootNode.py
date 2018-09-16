#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Generator

from jsonpath2.Node import MatchData, Node

class RootNode(Node):
    def __init__(self, next_node:Node):
        super(RootNode, self).__init__()

        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield '$'

        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        return map(lambda next_node_match_data: MatchData(RootNode(next_node_match_data.node), next_node_match_data.root_value, next_node_match_data.current_value), self.next_node.match(root_value, root_value))
