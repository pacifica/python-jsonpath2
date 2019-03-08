grammar JSONPath;

CURRENT_VALUE : '@' ;
RECURSIVE_DESCENT : '..' ;
ROOT_VALUE : '$' ;
SUBSCRIPT : '.' ;
WILDCARD_SUBSCRIPT : '*' ;

AND : 'and' ;
EQ : '=' ;
GE : '>=' ;
GT : '>' ;
LE : '<=' ;
LT : '<' ;
NE : '!=' ;
NOT : 'not' ;
OR : 'or' ;

TRUE : 'true' ;
FALSE : 'false' ;
NULL : 'null' ;

BRACE_LEFT : '{' ;
BRACE_RIGHT : '}' ;
BRACKET_LEFT : '[' ;
BRACKET_RIGHT : ']' ;
COLON : ':' ;
COMMA : ',' ;
PAREN_LEFT : '(' ;
PAREN_RIGHT : ')' ;
QUESTION : '?' ;

jsonpath
   : ROOT_VALUE subscript? EOF
   ;

jsonpath_
   : ( ROOT_VALUE | CURRENT_VALUE ) subscript?
   ;

jsonpath__
   : jsonpath_
   | value
   ;


subscript
   : RECURSIVE_DESCENT ( subscriptableBareword | subscriptables ) subscript?
   | SUBSCRIPT subscriptableBareword subscript?
   | subscriptables subscript?
   ;

subscriptables
   : BRACKET_LEFT subscriptable ( COMMA subscriptable )* BRACKET_RIGHT
   ;

subscriptableArguments
   : PAREN_LEFT ( jsonpath__ ( COMMA jsonpath__ )* )? PAREN_RIGHT
   ;

subscriptableBareword
   : ID subscriptableArguments?
   | WILDCARD_SUBSCRIPT
   ;

subscriptable
   : STRING
   | NUMBER{self.tryCast(int)}? sliceable?
   | sliceable
   | WILDCARD_SUBSCRIPT
   | QUESTION PAREN_LEFT expression PAREN_RIGHT
   | jsonpath_
   | ID subscriptableArguments
   ;

sliceable
   : COLON ( NUMBER{self.tryCast(int)}? )? ( COLON NUMBER{self.tryCast(int)}? )?
   ;

expression
   : andExpression
   ;

andExpression
   : orExpression ( AND andExpression )?
   ;

orExpression
   : notExpression ( OR orExpression )?
   ;

notExpression
   : NOT notExpression
   | PAREN_LEFT expression PAREN_RIGHT
   | jsonpath__ ( ( EQ | NE | LT | LE | GT | GE ) jsonpath__ )?
   ;


ID
   : [_A-Za-z] [_A-Za-z0-9]*
   ;


/* c.f., https://github.com/antlr/grammars-v4/blob/master/json/JSON.g4 */

json
   : value
   ;

obj
   : BRACE_LEFT pair ( COMMA pair )* BRACE_RIGHT
   | BRACE_LEFT BRACE_RIGHT
   ;

pair
   : STRING COLON value
   ;

array
   : BRACKET_LEFT value ( COMMA value )* BRACKET_RIGHT
   | BRACKET_LEFT BRACKET_RIGHT
   ;

value
   : STRING
   | NUMBER
   | obj
   | array
   | TRUE
   | FALSE
   | NULL
   ;


STRING
   : '"' (ESC | SAFECODEPOINT)* '"'
   ;


fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;


NUMBER
   : '-'? INT ('.' [0-9] +)? EXP?
   ;


fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;

// \- since - means "range" inside [...]

WS
   : [ \t\n\r] + -> skip
   ;
