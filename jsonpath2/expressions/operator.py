#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The operator expression module."""
import json
from typing import Callable, Generator, List
from jsonpath2.expression import Expression
from jsonpath2.node import Node


class OperatorExpression(Expression):
    """Basic operator expression object."""

    def __jsonpath__(self) -> Generator[str, None, None]:  # pragma: no cover abstract method
        """Abstract method to return the jsonpath."""
        pass

    def evaluate(self, root_value: object, current_value: object) -> bool:  # pragma: no cover abstract method
        """Abstract method to evaluate the expression."""
        pass


class BinaryOperatorExpression(OperatorExpression):
    """Binary operator expression."""

    def __init__(self, token: str, callback: Callable[[object, object], bool], left_node: Node, right_value: object):
        """Constructor save the left right and token."""
        super(BinaryOperatorExpression, self).__init__()
        self.token = token
        self.callback = callback
        self.left_node = left_node
        self.right_value = right_value

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Return the string json path of this expression."""
        for left_node_token in self.left_node.__jsonpath__():
            yield left_node_token
        yield ' '
        yield self.token
        yield ' '
        yield json.dumps(self.right_value)

    def evaluate(self, root_value: object, current_value: object) -> bool:
        """Evaluate the left and right values given the token."""
        return any(
            map(
                lambda left_node_match_data: self.callback(
                    left_node_match_data.current_value,
                    self.right_value
                ),
                self.left_node.match(root_value, current_value)
            )
        )


class EqualBinaryOperatorExpression(BinaryOperatorExpression):
    """Binary Equal operator expression."""

    def __init__(self, *args, **kwargs):
        """Constructor with the right function."""
        super(EqualBinaryOperatorExpression, self).__init__(
            '=', EqualBinaryOperatorExpression.__evaluate__,
            *args, **kwargs)

    @staticmethod
    def __evaluate__(x_obj, y_obj):
        """Perform an equal on int or float."""
        return x_obj == y_obj


class NotEqualBinaryOperatorExpression(BinaryOperatorExpression):
    """Binary Equal operator expression."""

    def __init__(self, *args, **kwargs):
        """Constructor with the right function."""
        super(NotEqualBinaryOperatorExpression, self).__init__(
            '!=', NotEqualBinaryOperatorExpression.__evaluate__,
            *args, **kwargs)

    @staticmethod
    def __evaluate__(x_obj, y_obj):
        """Perform a not equal on int or float."""
        return x_obj != y_obj


class LessThanBinaryOperatorExpression(BinaryOperatorExpression):
    """Expression to handle less than."""

    def __init__(self, *args, **kwargs):
        """Construct the binary operator with appropriate method."""
        super(LessThanBinaryOperatorExpression, self).__init__(
            '<', LessThanBinaryOperatorExpression.__evaluate__, *args, **kwargs)

    @staticmethod
    def __evaluate__(x_obj, y_obj):
        """Perform a less than on int or float."""
        if isinstance(x_obj, (float, int)) and isinstance(y_obj, (float, int)):
            return x_obj < y_obj
        return False


class LessThanOrEqualToBinaryOperatorExpression(BinaryOperatorExpression):
    """Expression to handle less than or equal."""

    def __init__(self, *args, **kwargs):
        """Construct the binary operator with appropriate method."""
        super(LessThanOrEqualToBinaryOperatorExpression, self).__init__(
            '<=', LessThanOrEqualToBinaryOperatorExpression.__evaluate__, *args, **kwargs)

    @staticmethod
    def __evaluate__(x_obj, y_obj):
        """Perform a less than or equal to on int or float."""
        if isinstance(x_obj, (float, int)) and isinstance(y_obj, (float, int)):
            return x_obj <= y_obj
        return False


class GreaterThanBinaryOperatorExpression(BinaryOperatorExpression):
    """Expression to handle greater than."""

    def __init__(self, *args, **kwargs):
        """Construct the binary operator with appropriate method."""
        super(GreaterThanBinaryOperatorExpression, self).__init__(
            '>', GreaterThanBinaryOperatorExpression.__evaluate__, *args, **kwargs)

    @staticmethod
    def __evaluate__(x_obj, y_obj):
        """Perform a greater than on int or float."""
        if isinstance(x_obj, (float, int)) and isinstance(y_obj, (float, int)):
            return x_obj > y_obj
        return False


class GreaterThanOrEqualToBinaryOperatorExpression(BinaryOperatorExpression):
    """Expression to handle greater than or equal."""

    def __init__(self, *args, **kwargs):
        """Construct the binary operator with appropriate method."""
        super(GreaterThanOrEqualToBinaryOperatorExpression, self).__init__(
            '>=', GreaterThanOrEqualToBinaryOperatorExpression.__evaluate__, *args, **kwargs)

    @staticmethod
    def __evaluate__(x_obj, y_obj):
        """Perform a greater than or equal to on int or float."""
        if isinstance(x_obj, (float, int)) and isinstance(y_obj, (float, int)):
            return x_obj >= y_obj
        return False


class UnaryOperatorExpression(OperatorExpression):
    """Unary operator expression base class."""

    def __init__(self, token: str, callback: Callable[[bool], bool], expression: Expression):
        """Save the callback operator the token and expression."""
        super(UnaryOperatorExpression, self).__init__()
        self.token = token
        self.callback = callback
        self.expression = expression

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Generate the jsonpath for a unary operator."""
        yield self.token
        yield ' '
        if isinstance(self.expression, (UnaryOperatorExpression, VariadicOperatorExpression)):
            yield '('
        for expression_token in self.expression.__jsonpath__():
            yield expression_token
        if isinstance(self.expression, (UnaryOperatorExpression, VariadicOperatorExpression)):
            yield ')'

    def evaluate(self, root_value: object, current_value: object) -> bool:
        """Evaluate the unary expression."""
        return self.callback(self.expression.evaluate(root_value, current_value))


class NotUnaryOperatorExpression(UnaryOperatorExpression):
    """Unary class to handle the 'not' expression."""

    def __init__(self, *args, **kwargs):
        """Call the unary operator expression with the right method."""
        super(NotUnaryOperatorExpression, self).__init__(
            'not', NotUnaryOperatorExpression.__evaluate__, *args, **kwargs)

    @staticmethod
    def __evaluate__(x_obj):
        """The unary not function."""
        return not x_obj


class VariadicOperatorExpression(OperatorExpression):
    """Base class to handle boolean expressions of variadic type."""

    def __init__(self, token: str, callback: Callable[[List[bool]], bool], expressions: List[Expression] = None):
        """Save the operator token, callback and the list of expressions."""
        super(VariadicOperatorExpression, self).__init__()
        self.token = token
        self.callback = callback
        self.expressions = expressions if expressions else []

    def __jsonpath__(self) -> Generator[str, None, None]:
        """Yield the string of the expression."""
        expressions_count = len(self.expressions)
        if expressions_count == 0:
            pass
        elif expressions_count == 1:
            for expression_token in self.expressions[0].__jsonpath__():
                yield expression_token
        else:
            for expression_index, expression in enumerate(self.expressions):
                if expression_index > 0:
                    yield ' '
                    yield self.token
                    yield ' '

                if isinstance(expression, VariadicOperatorExpression):
                    yield '('

                for expression_token in expression.__jsonpath__():
                    yield expression_token

                if isinstance(expression, VariadicOperatorExpression):
                    yield ')'

    def evaluate(self, root_value: object, current_value: object) -> bool:
        """Evaluate the expressions against the boolean callback."""
        return self.callback(map(lambda expression: expression.evaluate(root_value, current_value), self.expressions))


class AndVariadicOperatorExpression(VariadicOperatorExpression):
    """The boolean 'and' operator expression."""

    def __init__(self, *args, **kwargs):
        """Call the super with the 'and' boolean method."""
        super(AndVariadicOperatorExpression, self).__init__(
            'and', all, *args, **kwargs)


class OrVariadicOperatorExpression(VariadicOperatorExpression):
    """The boolean 'or' operator expression."""

    def __init__(self, *args, **kwargs):
        """Call the super with the 'or' boolean method."""
        super(OrVariadicOperatorExpression, self).__init__(
            'or', any, *args, **kwargs)
