# Generated from jsonpath2/parser/JSONPath.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,31,225,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,1,1,1,1,1,1,
        2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,8,1,
        8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,
        1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,5,27,158,8,27,10,27,12,27,
        161,9,27,1,28,1,28,1,28,5,28,166,8,28,10,28,12,28,169,9,28,1,28,
        1,28,1,29,1,29,1,29,3,29,176,8,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,31,1,31,1,32,1,32,1,33,3,33,189,8,33,1,33,1,33,1,33,4,33,194,8,
        33,11,33,12,33,195,3,33,198,8,33,1,33,3,33,201,8,33,1,34,1,34,1,
        34,5,34,206,8,34,10,34,12,34,209,9,34,3,34,211,8,34,1,35,1,35,3,
        35,215,8,35,1,35,1,35,1,36,4,36,220,8,36,11,36,12,36,221,1,36,1,
        36,0,0,37,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,0,61,0,63,0,65,0,67,30,
        69,0,71,0,73,31,1,0,10,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,
        95,97,122,8,0,34,34,47,47,92,92,98,98,102,102,110,110,114,114,116,
        116,3,0,48,57,65,70,97,102,3,0,0,31,34,34,92,92,1,0,48,57,1,0,49,
        57,2,0,69,69,101,101,2,0,43,43,45,45,3,0,9,10,13,13,32,32,230,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,
        0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,67,1,0,0,0,0,73,1,
        0,0,0,1,75,1,0,0,0,3,77,1,0,0,0,5,80,1,0,0,0,7,82,1,0,0,0,9,84,1,
        0,0,0,11,86,1,0,0,0,13,90,1,0,0,0,15,92,1,0,0,0,17,95,1,0,0,0,19,
        97,1,0,0,0,21,100,1,0,0,0,23,102,1,0,0,0,25,105,1,0,0,0,27,109,1,
        0,0,0,29,112,1,0,0,0,31,121,1,0,0,0,33,126,1,0,0,0,35,132,1,0,0,
        0,37,137,1,0,0,0,39,139,1,0,0,0,41,141,1,0,0,0,43,143,1,0,0,0,45,
        145,1,0,0,0,47,147,1,0,0,0,49,149,1,0,0,0,51,151,1,0,0,0,53,153,
        1,0,0,0,55,155,1,0,0,0,57,162,1,0,0,0,59,172,1,0,0,0,61,177,1,0,
        0,0,63,183,1,0,0,0,65,185,1,0,0,0,67,188,1,0,0,0,69,210,1,0,0,0,
        71,212,1,0,0,0,73,219,1,0,0,0,75,76,5,64,0,0,76,2,1,0,0,0,77,78,
        5,46,0,0,78,79,5,46,0,0,79,4,1,0,0,0,80,81,5,36,0,0,81,6,1,0,0,0,
        82,83,5,46,0,0,83,8,1,0,0,0,84,85,5,42,0,0,85,10,1,0,0,0,86,87,5,
        97,0,0,87,88,5,110,0,0,88,89,5,100,0,0,89,12,1,0,0,0,90,91,5,61,
        0,0,91,14,1,0,0,0,92,93,5,62,0,0,93,94,5,61,0,0,94,16,1,0,0,0,95,
        96,5,62,0,0,96,18,1,0,0,0,97,98,5,60,0,0,98,99,5,61,0,0,99,20,1,
        0,0,0,100,101,5,60,0,0,101,22,1,0,0,0,102,103,5,33,0,0,103,104,5,
        61,0,0,104,24,1,0,0,0,105,106,5,110,0,0,106,107,5,111,0,0,107,108,
        5,116,0,0,108,26,1,0,0,0,109,110,5,111,0,0,110,111,5,114,0,0,111,
        28,1,0,0,0,112,113,5,99,0,0,113,114,5,111,0,0,114,115,5,110,0,0,
        115,116,5,116,0,0,116,117,5,97,0,0,117,118,5,105,0,0,118,119,5,110,
        0,0,119,120,5,115,0,0,120,30,1,0,0,0,121,122,5,116,0,0,122,123,5,
        114,0,0,123,124,5,117,0,0,124,125,5,101,0,0,125,32,1,0,0,0,126,127,
        5,102,0,0,127,128,5,97,0,0,128,129,5,108,0,0,129,130,5,115,0,0,130,
        131,5,101,0,0,131,34,1,0,0,0,132,133,5,110,0,0,133,134,5,117,0,0,
        134,135,5,108,0,0,135,136,5,108,0,0,136,36,1,0,0,0,137,138,5,123,
        0,0,138,38,1,0,0,0,139,140,5,125,0,0,140,40,1,0,0,0,141,142,5,91,
        0,0,142,42,1,0,0,0,143,144,5,93,0,0,144,44,1,0,0,0,145,146,5,58,
        0,0,146,46,1,0,0,0,147,148,5,44,0,0,148,48,1,0,0,0,149,150,5,40,
        0,0,150,50,1,0,0,0,151,152,5,41,0,0,152,52,1,0,0,0,153,154,5,63,
        0,0,154,54,1,0,0,0,155,159,7,0,0,0,156,158,7,1,0,0,157,156,1,0,0,
        0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,56,1,0,0,0,
        161,159,1,0,0,0,162,167,5,34,0,0,163,166,3,59,29,0,164,166,3,65,
        32,0,165,163,1,0,0,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,
        0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,171,5,34,
        0,0,171,58,1,0,0,0,172,175,5,92,0,0,173,176,7,2,0,0,174,176,3,61,
        30,0,175,173,1,0,0,0,175,174,1,0,0,0,176,60,1,0,0,0,177,178,5,117,
        0,0,178,179,3,63,31,0,179,180,3,63,31,0,180,181,3,63,31,0,181,182,
        3,63,31,0,182,62,1,0,0,0,183,184,7,3,0,0,184,64,1,0,0,0,185,186,
        8,4,0,0,186,66,1,0,0,0,187,189,5,45,0,0,188,187,1,0,0,0,188,189,
        1,0,0,0,189,190,1,0,0,0,190,197,3,69,34,0,191,193,5,46,0,0,192,194,
        7,5,0,0,193,192,1,0,0,0,194,195,1,0,0,0,195,193,1,0,0,0,195,196,
        1,0,0,0,196,198,1,0,0,0,197,191,1,0,0,0,197,198,1,0,0,0,198,200,
        1,0,0,0,199,201,3,71,35,0,200,199,1,0,0,0,200,201,1,0,0,0,201,68,
        1,0,0,0,202,211,5,48,0,0,203,207,7,6,0,0,204,206,7,5,0,0,205,204,
        1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,211,
        1,0,0,0,209,207,1,0,0,0,210,202,1,0,0,0,210,203,1,0,0,0,211,70,1,
        0,0,0,212,214,7,7,0,0,213,215,7,8,0,0,214,213,1,0,0,0,214,215,1,
        0,0,0,215,216,1,0,0,0,216,217,3,69,34,0,217,72,1,0,0,0,218,220,7,
        9,0,0,219,218,1,0,0,0,220,221,1,0,0,0,221,219,1,0,0,0,221,222,1,
        0,0,0,222,223,1,0,0,0,223,224,6,36,0,0,224,74,1,0,0,0,13,0,159,165,
        167,175,188,195,197,200,207,210,214,221,1,6,0,0
    ]

class JSONPathLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CURRENT_VALUE = 1
    RECURSIVE_DESCENT = 2
    ROOT_VALUE = 3
    SUBSCRIPT = 4
    WILDCARD_SUBSCRIPT = 5
    AND = 6
    EQ = 7
    GE = 8
    GT = 9
    LE = 10
    LT = 11
    NE = 12
    NOT = 13
    OR = 14
    CN = 15
    TRUE = 16
    FALSE = 17
    NULL = 18
    BRACE_LEFT = 19
    BRACE_RIGHT = 20
    BRACKET_LEFT = 21
    BRACKET_RIGHT = 22
    COLON = 23
    COMMA = 24
    PAREN_LEFT = 25
    PAREN_RIGHT = 26
    QUESTION = 27
    ID = 28
    STRING = 29
    NUMBER = 30
    WS = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'@'", "'..'", "'$'", "'.'", "'*'", "'and'", "'='", "'>='", 
            "'>'", "'<='", "'<'", "'!='", "'not'", "'or'", "'contains'", 
            "'true'", "'false'", "'null'", "'{'", "'}'", "'['", "']'", "':'", 
            "','", "'('", "')'", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "CURRENT_VALUE", "RECURSIVE_DESCENT", "ROOT_VALUE", "SUBSCRIPT", 
            "WILDCARD_SUBSCRIPT", "AND", "EQ", "GE", "GT", "LE", "LT", "NE", 
            "NOT", "OR", "CN", "TRUE", "FALSE", "NULL", "BRACE_LEFT", "BRACE_RIGHT", 
            "BRACKET_LEFT", "BRACKET_RIGHT", "COLON", "COMMA", "PAREN_LEFT", 
            "PAREN_RIGHT", "QUESTION", "ID", "STRING", "NUMBER", "WS" ]

    ruleNames = [ "CURRENT_VALUE", "RECURSIVE_DESCENT", "ROOT_VALUE", "SUBSCRIPT", 
                  "WILDCARD_SUBSCRIPT", "AND", "EQ", "GE", "GT", "LE", "LT", 
                  "NE", "NOT", "OR", "CN", "TRUE", "FALSE", "NULL", "BRACE_LEFT", 
                  "BRACE_RIGHT", "BRACKET_LEFT", "BRACKET_RIGHT", "COLON", 
                  "COMMA", "PAREN_LEFT", "PAREN_RIGHT", "QUESTION", "ID", 
                  "STRING", "ESC", "UNICODE", "HEX", "SAFECODEPOINT", "NUMBER", 
                  "INT", "EXP", "WS" ]

    grammarFileName = "JSONPath.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


