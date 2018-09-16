# Generated from pacifica/jsonpath/parser/JSONPath.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("\u00a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\5\2!\n\2\3\2\3\2\3\3\3\3\3\3\5")
        buf.write("\3(\n\3\3\3\5\3+\n\3\3\3\3\3\3\3\5\3\60\n\3\3\3\3\3\5")
        buf.write("\3\64\n\3\5\3\66\n\3\3\4\3\4\3\4\3\4\7\4<\n\4\f\4\16\4")
        buf.write("?\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6K\n")
        buf.write("\6\3\6\3\6\3\6\5\6P\n\6\5\6R\n\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6Z\n\6\3\7\3\7\3\b\3\b\3\b\5\ba\n\b\3\t\3\t\3\t\5")
        buf.write("\tf\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\np\n\n\3\n\3")
        buf.write("\n\5\nt\n\n\5\nv\n\n\3\13\3\13\3\f\3\f\3\f\3\f\7\f~\n")
        buf.write("\f\f\f\16\f\u0081\13\f\3\f\3\f\3\f\3\f\5\f\u0087\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\7\16\u0091\n\16\f\16")
        buf.write("\16\16\u0094\13\16\3\16\3\16\3\16\3\16\5\16\u009a\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00a3\n\17\3")
        buf.write("\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\5\4\2")
        buf.write("\7\7\35\35\4\2\3\3\5\5\3\2\t\16\2\u00b4\2\36\3\2\2\2\4")
        buf.write("\65\3\2\2\2\6\67\3\2\2\2\bB\3\2\2\2\nY\3\2\2\2\f[\3\2")
        buf.write("\2\2\16]\3\2\2\2\20b\3\2\2\2\22u\3\2\2\2\24w\3\2\2\2\26")
        buf.write("\u0086\3\2\2\2\30\u0088\3\2\2\2\32\u0099\3\2\2\2\34\u00a2")
        buf.write("\3\2\2\2\36 \7\5\2\2\37!\5\4\3\2 \37\3\2\2\2 !\3\2\2\2")
        buf.write("!\"\3\2\2\2\"#\7\2\2\3#\3\3\2\2\2$\'\7\4\2\2%(\5\b\5\2")
        buf.write("&(\5\6\4\2\'%\3\2\2\2\'&\3\2\2\2(*\3\2\2\2)+\5\4\3\2*")
        buf.write(")\3\2\2\2*+\3\2\2\2+\66\3\2\2\2,-\7\6\2\2-/\5\b\5\2.\60")
        buf.write("\5\4\3\2/.\3\2\2\2/\60\3\2\2\2\60\66\3\2\2\2\61\63\5\6")
        buf.write("\4\2\62\64\5\4\3\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66\3")
        buf.write("\2\2\2\65$\3\2\2\2\65,\3\2\2\2\65\61\3\2\2\2\66\5\3\2")
        buf.write("\2\2\678\7\26\2\28=\5\n\6\29:\7\31\2\2:<\5\n\6\2;9\3\2")
        buf.write("\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?=\3\2\2\2")
        buf.write("@A\7\27\2\2A\7\3\2\2\2BC\t\2\2\2C\t\3\2\2\2DZ\7\36\2\2")
        buf.write("EF\7\37\2\2FQ\6\6\2\2GJ\7\30\2\2HI\7\37\2\2IK\6\6\3\2")
        buf.write("JH\3\2\2\2JK\3\2\2\2KO\3\2\2\2LM\7\30\2\2MN\7\37\2\2N")
        buf.write("P\6\6\4\2OL\3\2\2\2OP\3\2\2\2PR\3\2\2\2QG\3\2\2\2QR\3")
        buf.write("\2\2\2RZ\3\2\2\2SZ\7\7\2\2TU\7\34\2\2UV\7\32\2\2VW\5\f")
        buf.write("\7\2WX\7\33\2\2XZ\3\2\2\2YD\3\2\2\2YE\3\2\2\2YS\3\2\2")
        buf.write("\2YT\3\2\2\2Z\13\3\2\2\2[\\\5\16\b\2\\\r\3\2\2\2]`\5\20")
        buf.write("\t\2^_\7\b\2\2_a\5\16\b\2`^\3\2\2\2`a\3\2\2\2a\17\3\2")
        buf.write("\2\2be\5\22\n\2cd\7\20\2\2df\5\20\t\2ec\3\2\2\2ef\3\2")
        buf.write("\2\2f\21\3\2\2\2gh\7\17\2\2hv\5\22\n\2ij\7\32\2\2jk\5")
        buf.write("\f\7\2kl\7\33\2\2lv\3\2\2\2mo\t\3\2\2np\5\4\3\2on\3\2")
        buf.write("\2\2op\3\2\2\2ps\3\2\2\2qr\t\4\2\2rt\5\34\17\2sq\3\2\2")
        buf.write("\2st\3\2\2\2tv\3\2\2\2ug\3\2\2\2ui\3\2\2\2um\3\2\2\2v")
        buf.write("\23\3\2\2\2wx\5\34\17\2x\25\3\2\2\2yz\7\24\2\2z\177\5")
        buf.write("\30\r\2{|\7\31\2\2|~\5\30\r\2}{\3\2\2\2~\u0081\3\2\2\2")
        buf.write("\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0082\u0083\7\25\2\2\u0083\u0087\3\2\2\2")
        buf.write("\u0084\u0085\7\24\2\2\u0085\u0087\7\25\2\2\u0086y\3\2")
        buf.write("\2\2\u0086\u0084\3\2\2\2\u0087\27\3\2\2\2\u0088\u0089")
        buf.write("\7\36\2\2\u0089\u008a\7\30\2\2\u008a\u008b\5\34\17\2\u008b")
        buf.write("\31\3\2\2\2\u008c\u008d\7\26\2\2\u008d\u0092\5\34\17\2")
        buf.write("\u008e\u008f\7\31\2\2\u008f\u0091\5\34\17\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0095\u0096\7\27\2\2\u0096\u009a\3\2\2\2\u0097\u0098")
        buf.write("\7\26\2\2\u0098\u009a\7\27\2\2\u0099\u008c\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u009a\33\3\2\2\2\u009b\u00a3\7\36\2\2\u009c")
        buf.write("\u00a3\7\37\2\2\u009d\u00a3\5\26\f\2\u009e\u00a3\5\32")
        buf.write("\16\2\u009f\u00a3\7\21\2\2\u00a0\u00a3\7\22\2\2\u00a1")
        buf.write("\u00a3\7\23\2\2\u00a2\u009b\3\2\2\2\u00a2\u009c\3\2\2")
        buf.write("\2\u00a2\u009d\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2\u009f")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3")
        buf.write("\35\3\2\2\2\27 \'*/\63\65=JOQY`eosu\177\u0086\u0092\u0099")
        buf.write("\u00a2")
        return buf.getvalue()


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
    RULE_subscript = 1
    RULE_subscriptables = 2
    RULE_subscriptableBareword = 3
    RULE_subscriptable = 4
    RULE_expression = 5
    RULE_andExpression = 6
    RULE_orExpression = 7
    RULE_notExpression = 8
    RULE_json = 9
    RULE_obj = 10
    RULE_pair = 11
    RULE_array = 12
    RULE_value = 13

    ruleNames =  [ "jsonpath", "subscript", "subscriptables", "subscriptableBareword", 
                   "subscriptable", "expression", "andExpression", "orExpression", 
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
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonpathContext(ParserRuleContext):

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
            self.state = 28
            self.match(JSONPathParser.ROOT_VALUE)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                self.state = 29
                self.subscript()


            self.state = 32
            self.match(JSONPathParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptContext(ParserRuleContext):

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
        self.enterRule(localctx, 2, self.RULE_subscript)
        self._la = 0 # Token type
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.RECURSIVE_DESCENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(JSONPathParser.RECURSIVE_DESCENT)
                self.state = 37
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JSONPathParser.WILDCARD_SUBSCRIPT, JSONPathParser.ID]:
                    self.state = 35
                    self.subscriptableBareword()
                    pass
                elif token in [JSONPathParser.BRACKET_LEFT]:
                    self.state = 36
                    self.subscriptables()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                    self.state = 39
                    self.subscript()


                pass
            elif token in [JSONPathParser.SUBSCRIPT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(JSONPathParser.SUBSCRIPT)
                self.state = 43
                self.subscriptableBareword()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                    self.state = 44
                    self.subscript()


                pass
            elif token in [JSONPathParser.BRACKET_LEFT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.subscriptables()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                    self.state = 48
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
        self.enterRule(localctx, 4, self.RULE_subscriptables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(JSONPathParser.BRACKET_LEFT)
            self.state = 54
            self.subscriptable()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSONPathParser.COMMA:
                self.state = 55
                self.match(JSONPathParser.COMMA)
                self.state = 56
                self.subscriptable()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(JSONPathParser.BRACKET_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptableBarewordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JSONPathParser.ID, 0)

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
        self.enterRule(localctx, 6, self.RULE_subscriptableBareword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==JSONPathParser.WILDCARD_SUBSCRIPT or _la==JSONPathParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.NUMBER)
            else:
                return self.getToken(JSONPathParser.NUMBER, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COLON)
            else:
                return self.getToken(JSONPathParser.COLON, i)

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
        self.enterRule(localctx, 8, self.RULE_subscriptable)
        self._la = 0 # Token type
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(JSONPathParser.NUMBER)
                self.state = 68
                if not self.tryCast(int):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.tryCast(int)")
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.COLON:
                    self.state = 69
                    self.match(JSONPathParser.COLON)
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.NUMBER:
                        self.state = 70
                        self.match(JSONPathParser.NUMBER)
                        self.state = 71
                        if not self.tryCast(int):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.tryCast(int)")


                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.COLON:
                        self.state = 74
                        self.match(JSONPathParser.COLON)
                        self.state = 75
                        self.match(JSONPathParser.NUMBER)
                        self.state = 76
                        if not self.tryCast(int):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.tryCast(int)")




                pass
            elif token in [JSONPathParser.WILDCARD_SUBSCRIPT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(JSONPathParser.WILDCARD_SUBSCRIPT)
                pass
            elif token in [JSONPathParser.QUESTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.match(JSONPathParser.QUESTION)
                self.state = 83
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 84
                self.expression()
                self.state = 85
                self.match(JSONPathParser.PAREN_RIGHT)
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

    class ExpressionContext(ParserRuleContext):

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
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.andExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AndExpressionContext(ParserRuleContext):

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
        self.enterRule(localctx, 12, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.orExpression()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.AND:
                self.state = 92
                self.match(JSONPathParser.AND)
                self.state = 93
                self.andExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OrExpressionContext(ParserRuleContext):

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
        self.enterRule(localctx, 14, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.notExpression()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.OR:
                self.state = 97
                self.match(JSONPathParser.OR)
                self.state = 98
                self.orExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NotExpressionContext(ParserRuleContext):

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

        def ROOT_VALUE(self):
            return self.getToken(JSONPathParser.ROOT_VALUE, 0)

        def CURRENT_VALUE(self):
            return self.getToken(JSONPathParser.CURRENT_VALUE, 0)

        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


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
        self.enterRule(localctx, 16, self.RULE_notExpression)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(JSONPathParser.NOT)
                self.state = 102
                self.notExpression()
                pass
            elif token in [JSONPathParser.PAREN_LEFT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 104
                self.expression()
                self.state = 105
                self.match(JSONPathParser.PAREN_RIGHT)
                pass
            elif token in [JSONPathParser.CURRENT_VALUE, JSONPathParser.ROOT_VALUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==JSONPathParser.CURRENT_VALUE or _la==JSONPathParser.ROOT_VALUE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.RECURSIVE_DESCENT) | (1 << JSONPathParser.SUBSCRIPT) | (1 << JSONPathParser.BRACKET_LEFT))) != 0):
                    self.state = 108
                    self.subscript()


                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0):
                    self.state = 111
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 112
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

    class JsonContext(ParserRuleContext):

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
        self.enterRule(localctx, 18, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

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
        self.enterRule(localctx, 20, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 120
                self.pair()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 121
                    self.match(JSONPathParser.COMMA)
                    self.state = 122
                    self.pair()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self.match(JSONPathParser.BRACE_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 131
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
        self.enterRule(localctx, 22, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(JSONPathParser.STRING)
            self.state = 135
            self.match(JSONPathParser.COLON)
            self.state = 136
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

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
        self.enterRule(localctx, 24, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 139
                self.value()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 140
                    self.match(JSONPathParser.COMMA)
                    self.state = 141
                    self.value()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 147
                self.match(JSONPathParser.BRACKET_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 150
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
        self.enterRule(localctx, 26, self.RULE_value)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(JSONPathParser.NUMBER)
                pass
            elif token in [JSONPathParser.BRACE_LEFT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.obj()
                pass
            elif token in [JSONPathParser.BRACKET_LEFT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.array()
                pass
            elif token in [JSONPathParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 157
                self.match(JSONPathParser.TRUE)
                pass
            elif token in [JSONPathParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 158
                self.match(JSONPathParser.FALSE)
                pass
            elif token in [JSONPathParser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 159
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
        self._predicates[4] = self.subscriptable_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def subscriptable_sempred(self, localctx:SubscriptableContext, predIndex:int):
            if predIndex == 0:
                return self.tryCast(int)
         

            if predIndex == 1:
                return self.tryCast(int)
         

            if predIndex == 2:
                return self.tryCast(int)
         




