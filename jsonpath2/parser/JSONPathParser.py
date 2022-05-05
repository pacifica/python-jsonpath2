# Generated from jsonpath2/parser/JSONPath.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,3,0,39,8,0,1,0,1,
        0,1,1,1,1,3,1,45,8,1,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,3,3,54,8,3,1,
        3,3,3,57,8,3,1,3,1,3,1,3,3,3,62,8,3,1,3,1,3,3,3,66,8,3,3,3,68,8,
        3,1,4,1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,1,5,1,5,1,
        5,1,5,5,5,85,8,5,10,5,12,5,88,9,5,3,5,90,8,5,1,5,1,5,1,6,1,6,3,6,
        96,8,6,1,6,3,6,99,8,6,1,7,1,7,1,7,1,7,3,7,105,8,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,117,8,7,1,8,1,8,1,8,3,8,122,8,8,1,
        8,1,8,1,8,3,8,127,8,8,3,8,129,8,8,1,9,1,9,1,10,1,10,1,10,3,10,136,
        8,10,1,11,1,11,1,11,3,11,141,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,3,12,152,8,12,3,12,154,8,12,1,13,1,13,1,14,1,14,1,
        14,1,14,5,14,162,8,14,10,14,12,14,165,9,14,1,14,1,14,1,14,1,14,3,
        14,171,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,181,8,16,
        10,16,12,16,184,9,16,1,16,1,16,1,16,1,16,3,16,190,8,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,199,8,17,1,17,0,0,18,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,0,2,2,0,1,1,3,3,1,0,7,12,221,
        0,36,1,0,0,0,2,42,1,0,0,0,4,48,1,0,0,0,6,67,1,0,0,0,8,69,1,0,0,0,
        10,80,1,0,0,0,12,98,1,0,0,0,14,116,1,0,0,0,16,118,1,0,0,0,18,130,
        1,0,0,0,20,132,1,0,0,0,22,137,1,0,0,0,24,153,1,0,0,0,26,155,1,0,
        0,0,28,170,1,0,0,0,30,172,1,0,0,0,32,189,1,0,0,0,34,198,1,0,0,0,
        36,38,5,3,0,0,37,39,3,6,3,0,38,37,1,0,0,0,38,39,1,0,0,0,39,40,1,
        0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,44,7,0,0,0,43,45,3,6,3,0,44,
        43,1,0,0,0,44,45,1,0,0,0,45,3,1,0,0,0,46,49,3,2,1,0,47,49,3,34,17,
        0,48,46,1,0,0,0,48,47,1,0,0,0,49,5,1,0,0,0,50,53,5,2,0,0,51,54,3,
        12,6,0,52,54,3,8,4,0,53,51,1,0,0,0,53,52,1,0,0,0,54,56,1,0,0,0,55,
        57,3,6,3,0,56,55,1,0,0,0,56,57,1,0,0,0,57,68,1,0,0,0,58,59,5,4,0,
        0,59,61,3,12,6,0,60,62,3,6,3,0,61,60,1,0,0,0,61,62,1,0,0,0,62,68,
        1,0,0,0,63,65,3,8,4,0,64,66,3,6,3,0,65,64,1,0,0,0,65,66,1,0,0,0,
        66,68,1,0,0,0,67,50,1,0,0,0,67,58,1,0,0,0,67,63,1,0,0,0,68,7,1,0,
        0,0,69,70,5,20,0,0,70,75,3,14,7,0,71,72,5,23,0,0,72,74,3,14,7,0,
        73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,
        0,0,0,77,75,1,0,0,0,78,79,5,21,0,0,79,9,1,0,0,0,80,89,5,24,0,0,81,
        86,3,4,2,0,82,83,5,23,0,0,83,85,3,4,2,0,84,82,1,0,0,0,85,88,1,0,
        0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,89,81,
        1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,25,0,0,92,11,1,0,0,0,
        93,95,5,27,0,0,94,96,3,10,5,0,95,94,1,0,0,0,95,96,1,0,0,0,96,99,
        1,0,0,0,97,99,5,5,0,0,98,93,1,0,0,0,98,97,1,0,0,0,99,13,1,0,0,0,
        100,117,5,28,0,0,101,102,5,29,0,0,102,104,4,7,0,0,103,105,3,16,8,
        0,104,103,1,0,0,0,104,105,1,0,0,0,105,117,1,0,0,0,106,117,3,16,8,
        0,107,117,5,5,0,0,108,109,5,26,0,0,109,110,5,24,0,0,110,111,3,18,
        9,0,111,112,5,25,0,0,112,117,1,0,0,0,113,117,3,2,1,0,114,115,5,27,
        0,0,115,117,3,10,5,0,116,100,1,0,0,0,116,101,1,0,0,0,116,106,1,0,
        0,0,116,107,1,0,0,0,116,108,1,0,0,0,116,113,1,0,0,0,116,114,1,0,
        0,0,117,15,1,0,0,0,118,121,5,22,0,0,119,120,5,29,0,0,120,122,4,8,
        1,0,121,119,1,0,0,0,121,122,1,0,0,0,122,128,1,0,0,0,123,126,5,22,
        0,0,124,125,5,29,0,0,125,127,4,8,2,0,126,124,1,0,0,0,126,127,1,0,
        0,0,127,129,1,0,0,0,128,123,1,0,0,0,128,129,1,0,0,0,129,17,1,0,0,
        0,130,131,3,20,10,0,131,19,1,0,0,0,132,135,3,22,11,0,133,134,5,6,
        0,0,134,136,3,20,10,0,135,133,1,0,0,0,135,136,1,0,0,0,136,21,1,0,
        0,0,137,140,3,24,12,0,138,139,5,14,0,0,139,141,3,22,11,0,140,138,
        1,0,0,0,140,141,1,0,0,0,141,23,1,0,0,0,142,143,5,13,0,0,143,154,
        3,24,12,0,144,145,5,24,0,0,145,146,3,18,9,0,146,147,5,25,0,0,147,
        154,1,0,0,0,148,151,3,4,2,0,149,150,7,1,0,0,150,152,3,4,2,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,142,1,0,0,0,153,
        144,1,0,0,0,153,148,1,0,0,0,154,25,1,0,0,0,155,156,3,34,17,0,156,
        27,1,0,0,0,157,158,5,18,0,0,158,163,3,30,15,0,159,160,5,23,0,0,160,
        162,3,30,15,0,161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,
        164,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,5,19,0,0,167,
        171,1,0,0,0,168,169,5,18,0,0,169,171,5,19,0,0,170,157,1,0,0,0,170,
        168,1,0,0,0,171,29,1,0,0,0,172,173,5,28,0,0,173,174,5,22,0,0,174,
        175,3,34,17,0,175,31,1,0,0,0,176,177,5,20,0,0,177,182,3,34,17,0,
        178,179,5,23,0,0,179,181,3,34,17,0,180,178,1,0,0,0,181,184,1,0,0,
        0,182,180,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,
        0,185,186,5,21,0,0,186,190,1,0,0,0,187,188,5,20,0,0,188,190,5,21,
        0,0,189,176,1,0,0,0,189,187,1,0,0,0,190,33,1,0,0,0,191,199,5,28,
        0,0,192,199,5,29,0,0,193,199,3,28,14,0,194,199,3,32,16,0,195,199,
        5,15,0,0,196,199,5,16,0,0,197,199,5,17,0,0,198,191,1,0,0,0,198,192,
        1,0,0,0,198,193,1,0,0,0,198,194,1,0,0,0,198,195,1,0,0,0,198,196,
        1,0,0,0,198,197,1,0,0,0,199,35,1,0,0,0,27,38,44,48,53,56,61,65,67,
        75,86,89,95,98,104,116,121,126,128,135,140,151,153,163,170,182,189,
        198
    ]

class JSONPathParser ( Parser ):

    grammarFileName = "JSONPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'..'", "'$'", "'.'", "'*'", "'and'",
                     "'='", "'>='", "'>'", "'<='", "'<'", "'!='", "'not'",
                     "'or'", "'true'", "'false'", "'null'", "'{'", "'}'",
                     "'['", "']'", "':'", "','", "'('", "')'", "'?'" ]

    symbolicNames = [ "<INVALID>", "CURRENT_VALUE", "RECURSIVE_DESCENT",
                      "ROOT_VALUE", "SUBSCRIPT", "WILDCARD_SUBSCRIPT", "AND",
                      "EQ", "GE", "GT", "LE", "LT", "NE", "NOT", "OR", "TRUE",
                      "FALSE", "NULL", "BRACE_LEFT", "BRACE_RIGHT", "BRACKET_LEFT",
                      "BRACKET_RIGHT", "COLON", "COMMA", "PAREN_LEFT", "PAREN_RIGHT",
                      "QUESTION", "ID", "STRING", "NUMBER", "WS" ]

    RULE_jsonpath = 0
    RULE_jsonpath_ = 1
    RULE_jsonpath__ = 2
    RULE_subscript = 3
    RULE_subscriptables = 4
    RULE_subscriptableArguments = 5
    RULE_subscriptableBareword = 6
    RULE_subscriptable = 7
    RULE_sliceable = 8
    RULE_expression = 9
    RULE_andExpression = 10
    RULE_orExpression = 11
    RULE_notExpression = 12
    RULE_json = 13
    RULE_obj = 14
    RULE_pair = 15
    RULE_array = 16
    RULE_value = 17

    ruleNames =  [ "jsonpath", "jsonpath_", "jsonpath__", "subscript", "subscriptables",
                   "subscriptableArguments", "subscriptableBareword", "subscriptable",
                   "sliceable", "expression", "andExpression", "orExpression",
                   "notExpression", "json", "obj", "pair", "array", "value" ]

    EOF = Token.EOF
    CURRENT_VALUE=1
    RECURSIVE_DESCENT=2
    ROOT_VALUE=3
    SUBSCRIPT=4
    WILDCARD_SUBSCRIPT=5
    AND=6
    EQ=7
    GE=8
    GT=9
    LE=10
    LT=11
    NE=12
    NOT=13
    OR=14
    TRUE=15
    FALSE=16
    NULL=17
    BRACE_LEFT=18
    BRACE_RIGHT=19
    BRACKET_LEFT=20
    BRACKET_RIGHT=21
    COLON=22
    COMMA=23
    PAREN_LEFT=24
    PAREN_RIGHT=25
    QUESTION=26
    ID=27
    STRING=28
    NUMBER=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT_VALUE(self):
            return self.getToken(JSONPathParser.ROOT_VALUE, 0)

        def EOF(self):
            return self.getToken(JSONPathParser.EOF, 0)

        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_jsonpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJsonpath" ):
                listener.enterJsonpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJsonpath" ):
                listener.exitJsonpath(self)




    def jsonpath(self):

        localctx = JSONPathParser.JsonpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_jsonpath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(JSONPathParser.ROOT_VALUE)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                self.state = 37
                self.subscript()


            self.state = 40
            self.match(JSONPathParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jsonpath_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT_VALUE(self):
            return self.getToken(JSONPathParser.ROOT_VALUE, 0)

        def CURRENT_VALUE(self):
            return self.getToken(JSONPathParser.CURRENT_VALUE, 0)

        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_jsonpath_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJsonpath_" ):
                listener.enterJsonpath_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJsonpath_" ):
                listener.exitJsonpath_(self)




    def jsonpath_(self):

        localctx = JSONPathParser.Jsonpath_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_jsonpath_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==JSONPathParser.CURRENT_VALUE or _la==JSONPathParser.ROOT_VALUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                self.state = 43
                self.subscript()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jsonpath__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def jsonpath_(self):
            return self.getTypedRuleContext(JSONPathParser.Jsonpath_Context,0)


        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_jsonpath__

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJsonpath__" ):
                listener.enterJsonpath__(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJsonpath__" ):
                listener.exitJsonpath__(self)




    def jsonpath__(self):

        localctx = JSONPathParser.Jsonpath__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_jsonpath__)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.CURRENT_VALUE, JSONPathParser.ROOT_VALUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.jsonpath_()
                pass
            elif token in [JSONPathParser.TRUE, JSONPathParser.FALSE, JSONPathParser.NULL, JSONPathParser.BRACE_LEFT, JSONPathParser.BRACKET_LEFT, JSONPathParser.STRING, JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECURSIVE_DESCENT(self):
            return self.getToken(JSONPathParser.RECURSIVE_DESCENT, 0)

        def subscriptableBareword(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptableBarewordContext,0)


        def subscriptables(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptablesContext,0)


        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def SUBSCRIPT(self):
            return self.getToken(JSONPathParser.SUBSCRIPT, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_subscript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript" ):
                listener.enterSubscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript" ):
                listener.exitSubscript(self)




    def subscript(self):

        localctx = JSONPathParser.SubscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subscript)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.RECURSIVE_DESCENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(JSONPathParser.RECURSIVE_DESCENT)
                self.state = 53
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JSONPathParser.WILDCARD_SUBSCRIPT, JSONPathParser.ID]:
                    self.state = 51
                    self.subscriptableBareword()
                    pass
                elif token in [JSONPathParser.BRACKET_LEFT]:
                    self.state = 52
                    self.subscriptables()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                    self.state = 55
                    self.subscript()


                pass
            elif token in [JSONPathParser.SUBSCRIPT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(JSONPathParser.SUBSCRIPT)
                self.state = 59
                self.subscriptableBareword()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                    self.state = 60
                    self.subscript()


                pass
            elif token in [JSONPathParser.BRACKET_LEFT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.subscriptables()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                    self.state = 64
                    self.subscript()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_LEFT(self):
            return self.getToken(JSONPathParser.BRACKET_LEFT, 0)

        def subscriptable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.SubscriptableContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.SubscriptableContext,i)


        def BRACKET_RIGHT(self):
            return self.getToken(JSONPathParser.BRACKET_RIGHT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COMMA)
            else:
                return self.getToken(JSONPathParser.COMMA, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_subscriptables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptables" ):
                listener.enterSubscriptables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptables" ):
                listener.exitSubscriptables(self)




    def subscriptables(self):

        localctx = JSONPathParser.SubscriptablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subscriptables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(JSONPathParser.BRACKET_LEFT)
            self.state = 70
            self.subscriptable()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSONPathParser.COMMA:
                self.state = 71
                self.match(JSONPathParser.COMMA)
                self.state = 72
                self.subscriptable()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(JSONPathParser.BRACKET_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptableArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_LEFT(self):
            return self.getToken(JSONPathParser.PAREN_LEFT, 0)

        def PAREN_RIGHT(self):
            return self.getToken(JSONPathParser.PAREN_RIGHT, 0)

        def jsonpath__(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.Jsonpath__Context)
            else:
                return self.getTypedRuleContext(JSONPathParser.Jsonpath__Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COMMA)
            else:
                return self.getToken(JSONPathParser.COMMA, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_subscriptableArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptableArguments" ):
                listener.enterSubscriptableArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptableArguments" ):
                listener.exitSubscriptableArguments(self)




    def subscriptableArguments(self):

        localctx = JSONPathParser.SubscriptableArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_subscriptableArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(JSONPathParser.PAREN_LEFT)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.CURRENT_VALUE) | (1 << JSONPathParser.ROOT_VALUE) | (1 << JSONPathParser.TRUE) | (1 << JSONPathParser.FALSE) | (1 << JSONPathParser.NULL) | (1 << JSONPathParser.BRACE_LEFT) | (1 << JSONPathParser.BRACKET_LEFT) | (1 << JSONPathParser.STRING) | (1 << JSONPathParser.NUMBER))) != 0):
                self.state = 81
                self.jsonpath__()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 82
                    self.match(JSONPathParser.COMMA)
                    self.state = 83
                    self.jsonpath__()
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 91
            self.match(JSONPathParser.PAREN_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptableBarewordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JSONPathParser.ID, 0)

        def subscriptableArguments(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptableArgumentsContext,0)


        def WILDCARD_SUBSCRIPT(self):
            return self.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_subscriptableBareword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptableBareword" ):
                listener.enterSubscriptableBareword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptableBareword" ):
                listener.exitSubscriptableBareword(self)




    def subscriptableBareword(self):

        localctx = JSONPathParser.SubscriptableBarewordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subscriptableBareword)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(JSONPathParser.ID)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.PAREN_LEFT:
                    self.state = 94
                    self.subscriptableArguments()


                pass
            elif token in [JSONPathParser.WILDCARD_SUBSCRIPT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(JSONPathParser.WILDCARD_SUBSCRIPT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(JSONPathParser.NUMBER, 0)

        def sliceable(self):
            return self.getTypedRuleContext(JSONPathParser.SliceableContext,0)


        def WILDCARD_SUBSCRIPT(self):
            return self.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0)

        def QUESTION(self):
            return self.getToken(JSONPathParser.QUESTION, 0)

        def PAREN_LEFT(self):
            return self.getToken(JSONPathParser.PAREN_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(JSONPathParser.ExpressionContext,0)


        def PAREN_RIGHT(self):
            return self.getToken(JSONPathParser.PAREN_RIGHT, 0)

        def jsonpath_(self):
            return self.getTypedRuleContext(JSONPathParser.Jsonpath_Context,0)


        def ID(self):
            return self.getToken(JSONPathParser.ID, 0)

        def subscriptableArguments(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptableArgumentsContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_subscriptable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptable" ):
                listener.enterSubscriptable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptable" ):
                listener.exitSubscriptable(self)




    def subscriptable(self):

        localctx = JSONPathParser.SubscriptableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subscriptable)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(JSONPathParser.NUMBER)
                self.state = 102
                if not self.tryCast(int):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.tryCast(int)")
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.COLON:
                    self.state = 103
                    self.sliceable()


                pass
            elif token in [JSONPathParser.COLON]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.sliceable()
                pass
            elif token in [JSONPathParser.WILDCARD_SUBSCRIPT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(JSONPathParser.WILDCARD_SUBSCRIPT)
                pass
            elif token in [JSONPathParser.QUESTION]:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.match(JSONPathParser.QUESTION)
                self.state = 109
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 110
                self.expression()
                self.state = 111
                self.match(JSONPathParser.PAREN_RIGHT)
                pass
            elif token in [JSONPathParser.CURRENT_VALUE, JSONPathParser.ROOT_VALUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.jsonpath_()
                pass
            elif token in [JSONPathParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.match(JSONPathParser.ID)
                self.state = 115
                self.subscriptableArguments()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SliceableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COLON)
            else:
                return self.getToken(JSONPathParser.COLON, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.NUMBER)
            else:
                return self.getToken(JSONPathParser.NUMBER, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_sliceable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSliceable" ):
                listener.enterSliceable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSliceable" ):
                listener.exitSliceable(self)




    def sliceable(self):

        localctx = JSONPathParser.SliceableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sliceable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(JSONPathParser.COLON)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.NUMBER:
                self.state = 119
                self.match(JSONPathParser.NUMBER)
                self.state = 120
                if not self.tryCast(int):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.tryCast(int)")


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.COLON:
                self.state = 123
                self.match(JSONPathParser.COLON)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.NUMBER:
                    self.state = 124
                    self.match(JSONPathParser.NUMBER)
                    self.state = 125
                    if not self.tryCast(int):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.tryCast(int)")




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self):
            return self.getTypedRuleContext(JSONPathParser.AndExpressionContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = JSONPathParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.andExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpression(self):
            return self.getTypedRuleContext(JSONPathParser.OrExpressionContext,0)


        def AND(self):
            return self.getToken(JSONPathParser.AND, 0)

        def andExpression(self):
            return self.getTypedRuleContext(JSONPathParser.AndExpressionContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_andExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)




    def andExpression(self):

        localctx = JSONPathParser.AndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.orExpression()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.AND:
                self.state = 133
                self.match(JSONPathParser.AND)
                self.state = 134
                self.andExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpression(self):
            return self.getTypedRuleContext(JSONPathParser.NotExpressionContext,0)


        def OR(self):
            return self.getToken(JSONPathParser.OR, 0)

        def orExpression(self):
            return self.getTypedRuleContext(JSONPathParser.OrExpressionContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_orExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)




    def orExpression(self):

        localctx = JSONPathParser.OrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.notExpression()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.OR:
                self.state = 138
                self.match(JSONPathParser.OR)
                self.state = 139
                self.orExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(JSONPathParser.NOT, 0)

        def notExpression(self):
            return self.getTypedRuleContext(JSONPathParser.NotExpressionContext,0)


        def PAREN_LEFT(self):
            return self.getToken(JSONPathParser.PAREN_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(JSONPathParser.ExpressionContext,0)


        def PAREN_RIGHT(self):
            return self.getToken(JSONPathParser.PAREN_RIGHT, 0)

        def jsonpath__(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.Jsonpath__Context)
            else:
                return self.getTypedRuleContext(JSONPathParser.Jsonpath__Context,i)


        def EQ(self):
            return self.getToken(JSONPathParser.EQ, 0)

        def NE(self):
            return self.getToken(JSONPathParser.NE, 0)

        def LT(self):
            return self.getToken(JSONPathParser.LT, 0)

        def LE(self):
            return self.getToken(JSONPathParser.LE, 0)

        def GT(self):
            return self.getToken(JSONPathParser.GT, 0)

        def GE(self):
            return self.getToken(JSONPathParser.GE, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_notExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)




    def notExpression(self):

        localctx = JSONPathParser.NotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_notExpression)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(JSONPathParser.NOT)
                self.state = 143
                self.notExpression()
                pass
            elif token in [JSONPathParser.PAREN_LEFT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 145
                self.expression()
                self.state = 146
                self.match(JSONPathParser.PAREN_RIGHT)
                pass
            elif token in [JSONPathParser.CURRENT_VALUE, JSONPathParser.ROOT_VALUE, JSONPathParser.TRUE, JSONPathParser.FALSE, JSONPathParser.NULL, JSONPathParser.BRACE_LEFT, JSONPathParser.BRACKET_LEFT, JSONPathParser.STRING, JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.jsonpath__()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0):
                    self.state = 149
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 150
                    self.jsonpath__()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = JSONPathParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACE_LEFT(self):
            return self.getToken(JSONPathParser.BRACE_LEFT, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.PairContext,i)


        def BRACE_RIGHT(self):
            return self.getToken(JSONPathParser.BRACE_RIGHT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COMMA)
            else:
                return self.getToken(JSONPathParser.COMMA, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)




    def obj(self):

        localctx = JSONPathParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 158
                self.pair()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 159
                    self.match(JSONPathParser.COMMA)
                    self.state = 160
                    self.pair()
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 166
                self.match(JSONPathParser.BRACE_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 169
                self.match(JSONPathParser.BRACE_RIGHT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def COLON(self):
            return self.getToken(JSONPathParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = JSONPathParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(JSONPathParser.STRING)
            self.state = 173
            self.match(JSONPathParser.COLON)
            self.state = 174
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_LEFT(self):
            return self.getToken(JSONPathParser.BRACKET_LEFT, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.ValueContext,i)


        def BRACKET_RIGHT(self):
            return self.getToken(JSONPathParser.BRACKET_RIGHT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COMMA)
            else:
                return self.getToken(JSONPathParser.COMMA, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = JSONPathParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 177
                self.value()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 178
                    self.match(JSONPathParser.COMMA)
                    self.state = 179
                    self.value()
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 185
                self.match(JSONPathParser.BRACKET_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 188
                self.match(JSONPathParser.BRACKET_RIGHT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(JSONPathParser.NUMBER, 0)

        def obj(self):
            return self.getTypedRuleContext(JSONPathParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JSONPathParser.ArrayContext,0)


        def TRUE(self):
            return self.getToken(JSONPathParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(JSONPathParser.FALSE, 0)

        def NULL(self):
            return self.getToken(JSONPathParser.NULL, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = JSONPathParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_value)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(JSONPathParser.NUMBER)
                pass
            elif token in [JSONPathParser.BRACE_LEFT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.obj()
                pass
            elif token in [JSONPathParser.BRACKET_LEFT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.array()
                pass
            elif token in [JSONPathParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.match(JSONPathParser.TRUE)
                pass
            elif token in [JSONPathParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.match(JSONPathParser.FALSE)
                pass
            elif token in [JSONPathParser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 197
                self.match(JSONPathParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.subscriptable_sempred
        self._predicates[8] = self.sliceable_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def subscriptable_sempred(self, localctx:SubscriptableContext, predIndex:int):
            if predIndex == 0:
                return self.tryCast(int)


    def sliceable_sempred(self, localctx:SliceableContext, predIndex:int):
            if predIndex == 1:
                return self.tryCast(int)


            if predIndex == 2:
                return self.tryCast(int)
