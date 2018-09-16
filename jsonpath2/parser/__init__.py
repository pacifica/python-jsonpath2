#!/usr/bin/python
# -*- coding: utf-8 -*-

import antlr4

from jsonpath2.expressions.OperatorExpression import AndVariadicOperatorExpression, EqualBinaryOperatorExpression, GreaterThanBinaryOperatorExpression, GreaterThanOrEqualToBinaryOperatorExpression, LessThanBinaryOperatorExpression, LessThanOrEqualToBinaryOperatorExpression, NotEqualBinaryOperatorExpression, NotUnaryOperatorExpression, OrVariadicOperatorExpression
from jsonpath2.expressions.SomeExpression import SomeExpression

from jsonpath2.nodes.CurrentNode import CurrentNode
from jsonpath2.nodes.RecursiveDescentNode import RecursiveDescentNode
from jsonpath2.nodes.RootNode import RootNode
from jsonpath2.nodes.SubscriptNode import SubscriptNode
from jsonpath2.nodes.TerminalNode import TerminalNode

from jsonpath2.parser.JSONPathLexer import JSONPathLexer
from jsonpath2.parser.JSONPathListener import JSONPathListener
from jsonpath2.parser.JSONPathParser import JSONPathParser

from jsonpath2.subscripts.ArrayIndexSubscript import ArrayIndexSubscript
from jsonpath2.subscripts.ArraySliceSubscript import ArraySliceSubscript
from jsonpath2.subscripts.FilterSubscript import FilterSubscript
from jsonpath2.subscripts.ObjectIndexSubscript import ObjectIndexSubscript
from jsonpath2.subscripts.WildcardSubscript import WildcardSubscript

class _ConsoleErrorListener(antlr4.error.ErrorListener.ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError('line {}:{} {}'.format(line, column, msg))

class _JSONPathListener(JSONPathListener):
    def __init__(self, _stack=[]):
        super(_JSONPathListener, self).__init__()

        self._stack = _stack

    def exitJsonpath(self, ctx:JSONPathParser.JsonpathContext):
        if ctx.getToken(JSONPathParser.ROOT_VALUE, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            self._stack.append(RootNode(next_node))
        else:
            raise ValueError()

    def exitSubscript(self, ctx:JSONPathParser.SubscriptContext):
        if ctx.getToken(JSONPathParser.RECURSIVE_DESCENT, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            if bool(ctx.subscriptableBareword()):
                subscriptable_nodes = [self._stack.pop()]
            elif bool(ctx.subscriptables()):
                subscriptable_nodes = self._stack.pop()
            else:
                raise ValueError()

            self._stack.append(RecursiveDescentNode(SubscriptNode(next_node, subscriptable_nodes)))
        elif ctx.getToken(JSONPathParser.SUBSCRIPT, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            if bool(ctx.subscriptableBareword()):
                subscriptable_nodes = [self._stack.pop()]
            else:
                raise ValueError()

            self._stack.append(SubscriptNode(next_node, subscriptable_nodes))
        else:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            if bool(ctx.subscriptables()):
                subscriptable_nodes = self._stack.pop()
            else:
                raise ValueError()

            self._stack.append(SubscriptNode(next_node, subscriptable_nodes))

    def exitSubscriptables(self, ctx:JSONPathParser.SubscriptablesContext):
        subscriptable_nodes = []

        for subscriptable_ctx in ctx.getTypedRuleContexts(JSONPathParser.SubscriptableContext):
            subscriptable_node = self._stack.pop()

            subscriptable_nodes.insert(0, subscriptable_node)

        self._stack.append(subscriptable_nodes)

    def exitSubscriptableBareword(self, ctx:JSONPathParser.SubscriptableBarewordContext):
        if bool(ctx.ID()):
            text = ctx.ID().getText()

            self._stack.append(ObjectIndexSubscript(text))
        elif ctx.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0) is not None:
            self._stack.append(WildcardSubscript())
        else:
            raise ValueError()

    def exitSubscriptable(self, ctx:JSONPathParser.SubscriptableContext):
        if bool(ctx.STRING()):
            text = ctx.STRING().getText()[1:-1]

            self._stack.append(ObjectIndexSubscript(text))
        elif bool(ctx.NUMBER()):
            if ctx.getToken(JSONPathParser.COLON, 0) is not None:
                start = int(ctx.NUMBER(0).getText()) if bool(ctx.NUMBER(0)) else None

                end = int(ctx.NUMBER(1).getText()) if bool(ctx.NUMBER(1)) else None

                step = int(ctx.NUMBER(2).getText()) if bool(ctx.NUMBER(2)) else None

                self._stack.append(ArraySliceSubscript(start, end, step))
            else:
                index = int(ctx.NUMBER(0).getText())

                self._stack.append(ArrayIndexSubscript(index))
        elif ctx.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0) is not None:
            self._stack.append(WildcardSubscript())
        elif ctx.getToken(JSONPathParser.QUESTION, 0) is not None:
            expression = self._stack.pop()

            self._stack.append(FilterSubscript(expression))
        else:
            raise ValueError()

    def exitAndExpression(self, ctx:JSONPathParser.AndExpressionContext):
        expressions = []

        if bool(ctx.andExpression()):
            expression = self._stack.pop()

            if isinstance(expression, AndVariadicOperatorExpression):
                expressions = expression.expressions + expressions
            else:
                expressions.insert(0, expression)

        expression = self._stack.pop()

        if isinstance(expression, AndVariadicOperatorExpression):
            expressions = expression.expressions + expressions
        else:
            expressions.insert(0, expression)

        if len(expressions) == 0:
            raise ValueError()
        if len(expressions) == 1:
            self._stack.append(expressions[0])
        else:
            self._stack.append(AndVariadicOperatorExpression(expressions))

    def exitOrExpression(self, ctx:JSONPathParser.OrExpressionContext):
        expressions = []

        if bool(ctx.orExpression()):
            expression = self._stack.pop()

            if isinstance(expression, OrVariadicOperatorExpression):
                expressions = expression.expressions + expressions
            else:
                expressions.insert(0, expression)

        expression = self._stack.pop()

        if isinstance(expression, OrVariadicOperatorExpression):
            expressions = expression.expressions + expressions
        else:
            expressions.insert(0, expression)

        if len(expressions) == 0:
            raise ValueError()
        if len(expressions) == 1:
            self._stack.append(expressions[0])
        else:
            self._stack.append(OrVariadicOperatorExpression(expressions))

    def exitNotExpression(self, ctx:JSONPathParser.NotExpressionContext):
        if ctx.getToken(JSONPathParser.NOT, 0) is not None:
            expression = self._stack.pop()

            if isinstance(expression, NotUnaryOperatorExpression):
                self._stack.append(expression.expression)
            else:
                self._stack.append(NotUnaryOperatorExpression(expression))
        elif (ctx.getToken(JSONPathParser.ROOT_VALUE, 0) is not None) or (ctx.getToken(JSONPathParser.CURRENT_VALUE, 0) is not None):
            if bool(ctx.value()):
                right_value = self._stack.pop()

                if bool(ctx.subscript()):
                    next_node = self._stack.pop()
                else:
                    next_node = TerminalNode()

                if ctx.getToken(JSONPathParser.ROOT_VALUE, 0) is not None:
                    left_node = RootNode(next_node)
                elif ctx.getToken(JSONPathParser.CURRENT_VALUE, 0) is not None:
                    left_node = CurrentNode(next_node)
                else:
                    raise ValueError()

                if ctx.getToken(JSONPathParser.EQ, 0) is not None:
                    self._stack.append(EqualBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.NE, 0) is not None:
                    self._stack.append(NotEqualBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.LT, 0) is not None:
                    self._stack.append(LessThanBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.LE, 0) is not None:
                    self._stack.append(LessThanOrEqualToBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.GT, 0) is not None:
                    self._stack.append(GreaterThanBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.GE, 0) is not None:
                    self._stack.append(GreaterThanOrEqualToBinaryOperatorExpression(left_node, right_value))
                else:
                    raise ValueError()
            else:
                if bool(ctx.subscript()):
                    next_node = self._stack.pop()
                else:
                    next_node = TerminalNode()

                self._stack.append(SomeExpression(CurrentNode(next_node)))
        else:
            pass

    def exitObj(self, ctx:JSONPathParser.ObjContext):
        values = []

        for pair_ctx in ctx.getTypedRuleContexts(JSONPathParser.PairContext):
            value = self._stack.pop()

            values.insert(0, value)

        obj = {}

        for index, pair_ctx in enumerate(ctx.getTypedRuleContexts(JSONPathParser.PairContext)):
            key = pair_ctx.STRING().getText()[1:-1]

            obj[key] = values[index]

        self._stack.append(obj)

    def exitArray(self, ctx:JSONPathParser.ArrayContext):
        array = []

        for value_ctx in ctx.getTypedRuleContexts(JSONPathParser.ValueContext):
            value = self._stack.pop()

            array.insert(0, value)

        self._stack.append(array)

    def exitValue(self, ctx:JSONPathParser.ValueContext):
        if bool(ctx.STRING()):
            text = ctx.STRING().getText()[1:-1]

            self._stack.append(text)
        elif bool(ctx.NUMBER()):
            text = ctx.NUMBER().getText()

            if ('.' in text) or ('E' in text) or ('e' in text):
                self._stack.append(float(text))
            else:
                self._stack.append(int(text))
        elif bool(ctx.obj()):
            pass
        elif bool(ctx.array()):
            pass
        elif ctx.getToken(JSONPathParser.TRUE, 0) is not None:
            self._stack.append(True)
        elif ctx.getToken(JSONPathParser.FALSE, 0) is not None:
            self._stack.append(False)
        elif ctx.getToken(JSONPathParser.NULL, 0) is not None:
            self._stack.append(None)
        else:
            raise ValueError()

class _JSONPathParser(JSONPathParser):
    def tryCast(self, cls):
        try:
            cls(self._input.LT(-1).text)

            return True
        except ValueError:
            return False

def _parse_input_stream(input_stream:antlr4.InputStream) -> RootNode:
    error_listener = _ConsoleErrorListener()

    lexer = JSONPathLexer(input_stream)

    lexer.addErrorListener(error_listener)

    token_stream = antlr4.CommonTokenStream(lexer)

    parser = _JSONPathParser(token_stream)

    parser.addErrorListener(error_listener)

    tree = parser.jsonpath()

    listener = _JSONPathListener(_stack=[])

    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    return listener._stack.pop()

def parse_file(*args, **kwargs) -> RootNode:
    file_stream = antlr4.FileStream(*args, **kwargs)

    return _parse_input_stream(file_stream)

def parse_str(*args, **kwargs) -> RootNode:
    input_stream = antlr4.InputStream(*args, **kwargs)

    return _parse_input_stream(input_stream)
