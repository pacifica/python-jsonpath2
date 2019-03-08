# Generated from jsonpath2/parser/JSONPath.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONPathParser import JSONPathParser
else:
    from JSONPathParser import JSONPathParser

# This class defines a complete listener for a parse tree produced by JSONPathParser.
class JSONPathListener(ParseTreeListener):

    # Enter a parse tree produced by JSONPathParser#jsonpath.
    def enterJsonpath(self, ctx:JSONPathParser.JsonpathContext):
        pass

    # Exit a parse tree produced by JSONPathParser#jsonpath.
    def exitJsonpath(self, ctx:JSONPathParser.JsonpathContext):
        pass


    # Enter a parse tree produced by JSONPathParser#jsonpath_.
    def enterJsonpath_(self, ctx:JSONPathParser.Jsonpath_Context):
        pass

    # Exit a parse tree produced by JSONPathParser#jsonpath_.
    def exitJsonpath_(self, ctx:JSONPathParser.Jsonpath_Context):
        pass


    # Enter a parse tree produced by JSONPathParser#jsonpath__.
    def enterJsonpath__(self, ctx:JSONPathParser.Jsonpath__Context):
        pass

    # Exit a parse tree produced by JSONPathParser#jsonpath__.
    def exitJsonpath__(self, ctx:JSONPathParser.Jsonpath__Context):
        pass


    # Enter a parse tree produced by JSONPathParser#subscript.
    def enterSubscript(self, ctx:JSONPathParser.SubscriptContext):
        pass

    # Exit a parse tree produced by JSONPathParser#subscript.
    def exitSubscript(self, ctx:JSONPathParser.SubscriptContext):
        pass


    # Enter a parse tree produced by JSONPathParser#subscriptables.
    def enterSubscriptables(self, ctx:JSONPathParser.SubscriptablesContext):
        pass

    # Exit a parse tree produced by JSONPathParser#subscriptables.
    def exitSubscriptables(self, ctx:JSONPathParser.SubscriptablesContext):
        pass


    # Enter a parse tree produced by JSONPathParser#subscriptableArguments.
    def enterSubscriptableArguments(self, ctx:JSONPathParser.SubscriptableArgumentsContext):
        pass

    # Exit a parse tree produced by JSONPathParser#subscriptableArguments.
    def exitSubscriptableArguments(self, ctx:JSONPathParser.SubscriptableArgumentsContext):
        pass


    # Enter a parse tree produced by JSONPathParser#subscriptableBareword.
    def enterSubscriptableBareword(self, ctx:JSONPathParser.SubscriptableBarewordContext):
        pass

    # Exit a parse tree produced by JSONPathParser#subscriptableBareword.
    def exitSubscriptableBareword(self, ctx:JSONPathParser.SubscriptableBarewordContext):
        pass


    # Enter a parse tree produced by JSONPathParser#subscriptable.
    def enterSubscriptable(self, ctx:JSONPathParser.SubscriptableContext):
        pass

    # Exit a parse tree produced by JSONPathParser#subscriptable.
    def exitSubscriptable(self, ctx:JSONPathParser.SubscriptableContext):
        pass


    # Enter a parse tree produced by JSONPathParser#sliceable.
    def enterSliceable(self, ctx:JSONPathParser.SliceableContext):
        pass

    # Exit a parse tree produced by JSONPathParser#sliceable.
    def exitSliceable(self, ctx:JSONPathParser.SliceableContext):
        pass


    # Enter a parse tree produced by JSONPathParser#expression.
    def enterExpression(self, ctx:JSONPathParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JSONPathParser#expression.
    def exitExpression(self, ctx:JSONPathParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JSONPathParser#andExpression.
    def enterAndExpression(self, ctx:JSONPathParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by JSONPathParser#andExpression.
    def exitAndExpression(self, ctx:JSONPathParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by JSONPathParser#orExpression.
    def enterOrExpression(self, ctx:JSONPathParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by JSONPathParser#orExpression.
    def exitOrExpression(self, ctx:JSONPathParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by JSONPathParser#notExpression.
    def enterNotExpression(self, ctx:JSONPathParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by JSONPathParser#notExpression.
    def exitNotExpression(self, ctx:JSONPathParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by JSONPathParser#json.
    def enterJson(self, ctx:JSONPathParser.JsonContext):
        pass

    # Exit a parse tree produced by JSONPathParser#json.
    def exitJson(self, ctx:JSONPathParser.JsonContext):
        pass


    # Enter a parse tree produced by JSONPathParser#obj.
    def enterObj(self, ctx:JSONPathParser.ObjContext):
        pass

    # Exit a parse tree produced by JSONPathParser#obj.
    def exitObj(self, ctx:JSONPathParser.ObjContext):
        pass


    # Enter a parse tree produced by JSONPathParser#pair.
    def enterPair(self, ctx:JSONPathParser.PairContext):
        pass

    # Exit a parse tree produced by JSONPathParser#pair.
    def exitPair(self, ctx:JSONPathParser.PairContext):
        pass


    # Enter a parse tree produced by JSONPathParser#array.
    def enterArray(self, ctx:JSONPathParser.ArrayContext):
        pass

    # Exit a parse tree produced by JSONPathParser#array.
    def exitArray(self, ctx:JSONPathParser.ArrayContext):
        pass


    # Enter a parse tree produced by JSONPathParser#value.
    def enterValue(self, ctx:JSONPathParser.ValueContext):
        pass

    # Exit a parse tree produced by JSONPathParser#value.
    def exitValue(self, ctx:JSONPathParser.ValueContext):
        pass


