#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The jsonpath parser module."""
import antlr4
from jsonpath2.expressions.operator import AndVariadicOperatorExpression, EqualBinaryOperatorExpression, \
    GreaterThanBinaryOperatorExpression, GreaterThanOrEqualToBinaryOperatorExpression, \
    LessThanBinaryOperatorExpression, LessThanOrEqualToBinaryOperatorExpression, \
    NotEqualBinaryOperatorExpression, NotUnaryOperatorExpression, OrVariadicOperatorExpression
from jsonpath2.expressions.some import SomeExpression
from jsonpath2.nodes.current import CurrentNode
from jsonpath2.nodes.recursivedescent import RecursiveDescentNode
from jsonpath2.nodes.root import RootNode
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.nodes.terminal import TerminalNode

from jsonpath2.parser.JSONPathLexer import JSONPathLexer
from jsonpath2.parser.JSONPathListener import JSONPathListener
from jsonpath2.parser.JSONPathParser import JSONPathParser

from jsonpath2.subscripts.arrayindex import ArrayIndexSubscript
from jsonpath2.subscripts.arrayslice import ArraySliceSubscript
from jsonpath2.subscripts.callable import CallableSubscript
from jsonpath2.subscripts.filter import FilterSubscript
from jsonpath2.subscripts.node import NodeSubscript
from jsonpath2.subscripts.objectindex import ObjectIndexSubscript
from jsonpath2.subscripts.wildcard import WildcardSubscript


class CallableSubscriptNotFoundError(ValueError):
    """Callable subscript not found error."""

    def __init__(self, name):
        """Initialize callable subscript not found error."""
        super(CallableSubscriptNotFoundError, self).__init__()
        self.name = name

    def __str__(self):
        """Message."""
        return 'callable subscript \'{0}\' not found'.format(self.name.replace('\'', '\\\''))


CALLABLE_SUBSCRIPTS_ = {
    cls.__str__: cls
    for cls
    in CallableSubscript.__subclasses__()
}


# pylint: disable=invalid-name
def _createCallableSubscript(name, *args, **kwargs):
    """Create callable subscript for name, arguments and keyword arguments."""
    if name in CALLABLE_SUBSCRIPTS_:
        cls = CALLABLE_SUBSCRIPTS_[name]
        return cls(*args, **kwargs)
    raise CallableSubscriptNotFoundError(name)
# pylint: enable=invalid-name


class _ConsoleErrorListener(antlr4.error.ErrorListener.ConsoleErrorListener):
    # pylint: disable=too-many-arguments
    # this is an error handling issue with antlr
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError('line {}:{} {}'.format(line, column, msg))
    # pylint: enable=too-many-arguments


class _JSONPathListener(JSONPathListener):
    def __init__(self, _stack=None):
        super(_JSONPathListener, self).__init__()
        self._stack = _stack if _stack else []

    def exitJsonpath(self, ctx: JSONPathParser.JsonpathContext):
        if ctx.getToken(JSONPathParser.ROOT_VALUE, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()
            self._stack.append(RootNode(next_node))
        else:
            # NOTE Unreachable when listener is used as tree walker.
            raise ValueError()  # pragma: no cover

    def exitJsonpath_(self, ctx: JSONPathParser.JsonpathContext):
        if bool(ctx.subscript()):
            next_node = self._stack.pop()
        else:
            next_node = TerminalNode()

        if ctx.getToken(JSONPathParser.ROOT_VALUE, 0) is not None:
            self._stack.append(RootNode(next_node))
        elif ctx.getToken(JSONPathParser.CURRENT_VALUE, 0) is not None:
            self._stack.append(CurrentNode(next_node))
        else:
            # NOTE Unreachable when listener is used as tree walker.
            raise ValueError()  # pragma: no cover

    def exitJsonpath__(self, ctx: JSONPathParser.JsonpathContext):
        pass

    # pylint: disable=too-many-branches
    # It would sure be nice if we had a case statement.
    def exitSubscript(self, ctx: JSONPathParser.SubscriptContext):
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
                # NOTE Unreachable when listener is used as tree walker.
                raise ValueError()  # pragma: no cover
            self._stack.append(RecursiveDescentNode(
                SubscriptNode(next_node, subscriptable_nodes)))
        elif ctx.getToken(JSONPathParser.SUBSCRIPT, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()
            if bool(ctx.subscriptableBareword()):
                subscriptable_nodes = [self._stack.pop()]
            else:
                # NOTE Unreachable when listener is used as tree walker.
                raise ValueError()  # pragma: no cover
            self._stack.append(SubscriptNode(next_node, subscriptable_nodes))
        else:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()
            if bool(ctx.subscriptables()):
                subscriptable_nodes = self._stack.pop()
            else:
                # NOTE Unreachable when listener is used as tree walker.
                raise ValueError()  # pragma: no cover
            self._stack.append(SubscriptNode(next_node, subscriptable_nodes))
    # pylint: enable=too-many-branches

    def exitSubscriptables(self, ctx: JSONPathParser.SubscriptablesContext):
        subscriptable_nodes = []
        for _subscriptable_ctx in ctx.getTypedRuleContexts(JSONPathParser.SubscriptableContext):
            subscriptable_node = self._stack.pop()
            subscriptable_nodes.insert(0, subscriptable_node)
        self._stack.append(subscriptable_nodes)

    def exitSubscriptableArguments(self, ctx: JSONPathParser.SubscriptableArgumentsContext):
        args = []
        for _arg_ctx in ctx.getTypedRuleContexts(JSONPathParser.Jsonpath__Context):
            arg = self._stack.pop()
            args.insert(0, arg)
        self._stack.append(args)

    def exitSubscriptableBareword(self, ctx: JSONPathParser.SubscriptableBarewordContext):
        if bool(ctx.ID()):
            text = ctx.ID().getText()

            if bool(ctx.subscriptableArguments()):
                args = self._stack.pop()

                self._stack.append(_createCallableSubscript(text, *args))
            else:
                self._stack.append(ObjectIndexSubscript(text))
        elif ctx.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0) is not None:
            self._stack.append(WildcardSubscript())
        else:
            # NOTE Unreachable when listener is used as tree walker.
            raise ValueError()  # pragma: no cover

    def exitSubscriptable(self, ctx: JSONPathParser.SubscriptableContext):
        if bool(ctx.STRING()):
            text = ctx.STRING().getText()[1:-1]

            self._stack.append(ObjectIndexSubscript(text))
        elif bool(ctx.NUMBER()):
            if bool(ctx.sliceable()):
                func = self._stack.pop()

                start = int(ctx.NUMBER().getText()) if bool(
                    ctx.NUMBER()) else None

                self._stack.append(func(start))
            else:
                index = int(ctx.NUMBER().getText())

                self._stack.append(ArrayIndexSubscript(index))
        elif bool(ctx.sliceable()):
            func = self._stack.pop()

            start = None

            self._stack.append(func(start))
        elif ctx.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0) is not None:
            self._stack.append(WildcardSubscript())
        elif ctx.getToken(JSONPathParser.QUESTION, 0) is not None:
            expression = self._stack.pop()

            self._stack.append(FilterSubscript(expression))
        elif bool(ctx.jsonpath_()):
            next_node = self._stack.pop()

            self._stack.append(NodeSubscript(next_node))
        elif bool(ctx.ID()):
            text = ctx.ID().getText()

            args = self._stack.pop()

            self._stack.append(_createCallableSubscript(text, *args))
        else:
            # NOTE Unreachable when listener is used as tree walker.
            raise ValueError()  # pragma: no cover

    def exitSliceable(self, ctx: JSONPathParser.SliceableContext):
        end = int(ctx.NUMBER(0).getText()) if bool(
            ctx.NUMBER(0)) else None

        step = int(ctx.NUMBER(1).getText()) if bool(
            ctx.NUMBER(1)) else None

        self._stack.append(lambda start: ArraySliceSubscript(start, end, step))

    def exitAndExpression(self, ctx: JSONPathParser.AndExpressionContext):
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

        if not expressions:
            # NOTE Unreachable when listener is used as tree walker.
            raise ValueError()  # pragma: no cover
        if len(expressions) == 1:
            self._stack.append(expressions[0])
        else:
            self._stack.append(AndVariadicOperatorExpression(expressions))

    def exitOrExpression(self, ctx: JSONPathParser.OrExpressionContext):
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

        if not expressions:
            # NOTE Unreachable when listener is used as tree walker.
            raise ValueError()  # pragma: no cover
        if len(expressions) == 1:
            self._stack.append(expressions[0])
        else:
            self._stack.append(OrVariadicOperatorExpression(expressions))

    # pylint: disable=too-many-branches
    def exitNotExpression(self, ctx: JSONPathParser.NotExpressionContext):
        if bool(ctx.notExpression()):
            expression = self._stack.pop()

            if isinstance(expression, NotUnaryOperatorExpression):
                self._stack.append(expression.expression)
            else:
                self._stack.append(NotUnaryOperatorExpression(expression))
        elif bool(ctx.jsonpath__(1)):
            right_node_or_value = self._stack.pop()

            left_node_or_value = self._stack.pop()

            if ctx.getToken(JSONPathParser.EQ, 0) is not None:
                self._stack.append(
                    EqualBinaryOperatorExpression(left_node_or_value, right_node_or_value))
            elif ctx.getToken(JSONPathParser.NE, 0) is not None:
                self._stack.append(
                    NotEqualBinaryOperatorExpression(left_node_or_value, right_node_or_value))
            elif ctx.getToken(JSONPathParser.LT, 0) is not None:
                self._stack.append(
                    LessThanBinaryOperatorExpression(left_node_or_value, right_node_or_value))
            elif ctx.getToken(JSONPathParser.LE, 0) is not None:
                self._stack.append(
                    LessThanOrEqualToBinaryOperatorExpression(left_node_or_value, right_node_or_value))
            elif ctx.getToken(JSONPathParser.GT, 0) is not None:
                self._stack.append(
                    GreaterThanBinaryOperatorExpression(left_node_or_value, right_node_or_value))
            elif ctx.getToken(JSONPathParser.GE, 0) is not None:
                self._stack.append(
                    GreaterThanOrEqualToBinaryOperatorExpression(left_node_or_value, right_node_or_value))
            else:
                # NOTE Unreachable when listener is used as tree walker.
                raise ValueError()  # pragma: no cover
        elif bool(ctx.jsonpath__(0)):
            next_node_or_value = self._stack.pop()

            self._stack.append(SomeExpression(next_node_or_value))
        else:
            pass
    # pylint: enable=too-many-branches

    def exitObj(self, ctx: JSONPathParser.ObjContext):
        values = []

        for pair_ctx in ctx.getTypedRuleContexts(JSONPathParser.PairContext):
            value = self._stack.pop()

            values.insert(0, value)

        obj = {}

        for index, pair_ctx in enumerate(ctx.getTypedRuleContexts(JSONPathParser.PairContext)):
            key = pair_ctx.STRING().getText()[1:-1]

            obj[key] = values[index]

        self._stack.append(obj)

    def exitArray(self, ctx: JSONPathParser.ArrayContext):
        array = []

        for _value_ctx in ctx.getTypedRuleContexts(JSONPathParser.ValueContext):
            value = self._stack.pop()

            array.insert(0, value)

        self._stack.append(array)

    def exitValue(self, ctx: JSONPathParser.ValueContext):
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
        elif bool(ctx.TRUE()):
            self._stack.append(True)
        elif bool(ctx.FALSE()):
            self._stack.append(False)
        elif bool(ctx.NULL()):
            self._stack.append(None)
        else:
            # NOTE Unreachable when listener is used as tree walker.
            raise ValueError()  # pragma: no cover


class _JSONPathParser(JSONPathParser):
    # pylint: disable=invalid-name
    def tryCast(self, cls):
        """Override the antlr tryCast method."""
        try:
            cls(self._input.LT(-1).text)
            return True
        except ValueError:
            return False
    # pylint: enable=invalid-name


def _parse_input_stream(input_stream: antlr4.InputStream) -> RootNode:
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

    # pylint: disable=protected-access
    return listener._stack.pop()
    # pylint: enable=protected-access


def parse_file(*args, **kwargs) -> RootNode:
    """Parse a json path from a file."""
    file_stream = antlr4.FileStream(*args, **kwargs)
    return _parse_input_stream(file_stream)


def parse_str(*args, **kwargs) -> RootNode:
    """Parse a json path from a string."""
    input_stream = antlr4.InputStream(*args, **kwargs)
    return _parse_input_stream(input_stream)
