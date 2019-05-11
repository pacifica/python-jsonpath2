# jsonpath2
[![Build Status](https://travis-ci.org/pacifica/python-jsonpath2.svg?branch=master)](https://travis-ci.org/pacifica/python-jsonpath2)

This repository contains an implementation of [JSONPath](http://goessner.net/articles/JsonPath/) ([XPath](https://www.w3.org/TR/xpath/all/) for [JSON](https://www.json.org/)) for the Python programming language.

## API

### `Path` class

The `jsonpath2.path.Path` class represents a JSONPath.

```python
>>> s = '{"hello":"Hello, world!"}'
'{"hello":"Hello, world!"}'
>>> import json
>>> d = json.loads(s)
{'hello':'Hello, world!'}
>>> from jsonpath2.path import Path
>>> p = Path.parse_str('$["hello"]')
<jsonpath2.path.Path object>
>>> list(map(lambda match_data: match_data.current_value, p.match(d)))
['Hello, world!']
>>> list(map(lambda match_data: match_data.node.tojsonpath(), p.match(d)))
['$["hello"]']
```

This class is constructed with respect to the given instance of the `jsonpath2.nodes.root.RootNode` class (viz., the `root_node` property).

#### `parse_str(strdata)` class method

Parse the given string and return a new instance of this class.

#### `parse_file(fileName, encoding='ascii')` class method

Parse the contents of the given file and return a new instance of this class.

#### `match(root_value)` instance method

Match the given JSON data structure against this instance.
For each match, yield an instance of the `jsonpath2.node.MatchData` class.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `__str__()` instance method

Returns the string representation of this instance.

#### `root_node` property

The root node of the abstract syntax tree for this instance.

### `Node` abstract class

The `jsonpath2.node.Node` class represents the abstract syntax tree for a JSONPath.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `__jsonpath__()` instance method

Yields the lexer tokens for the string representation of this instance.

#### `match(root_value, current_value)` instance method

Match the given root and current JSON data structures against this instance.
For each match, yield an instance of the `jsonpath2.node.MatchData` class.

#### `tojsonpath()` instance method

Returns the string representation of this instance.

### `MatchData` class

The `jsonpath2.node.MatchData` class represents the JSON value and context for a JSONPath match.

This class is constructed with respect to a root JSON value, a current JSON value, and an abstract syntax tree node.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `root_value` property

The root JSON value.

#### `current_value` property

The current JSON value (i.e., the matching JSON value).

#### `node` property

The abstract syntax tree node.

## Syntax

| XPath | JSONPath | Description |
| - | - | - |
| `/` | `$` | the root JSON value |
| `.` | `@` | the current JSON value |
| `/` | `.` or `[]` | child operator |
| `//` | `..` | recursive descent (depth-first search) |
| `*` | `*` | wildcard (all elements of a JSON array; all values of a JSON object; otherwise none) |
| `[]` | `[]` | subscript operator |
| <code>&#124;</code> | `[,]` | union operator (for two or more subscript operators) |
| n/a | `[start:end:step]` | slice operator (subset of elements of a JSON array) |
| `[]` | `?()` | filter expression (for use with subscript operator) |

| JSONPath Filter Expression | Description |
| - | - |
| `$` or `@` | nested JSONPath (returns `true` if any match exists; otherwise, returns `false`) |
| `=`, `!=`, `>`, `>=`, `<`, `<=` | binary operator, where left- and right-hand operands are nested JSONPaths or JSON values (returns `true` if any match exists; otherwise, returns `false`) |
| `and`, `or`, `not` | Boolean operator, where operands are JSONPath filter expressions |
| `(` ... `)` | parentheses |

## Functions

Functions with the same API as https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference may be used as subscripts.

The syntax for a function call is the name of the function followed by the arguments in parentheses, i.e., `name(arg1, arg2, ..., argN)`, where the arguments are either JSONPaths or JSON values.

```python
>>> s = '{"hello":"Hello, world!"}'
'{"hello":"Hello, world!"}'
>>> import json
>>> d = json.loads(s)
{'hello':'Hello, world!'}
>>> from jsonpath2.path import Path
>>> p = Path.parse_str('$["hello"][length()]')
<jsonpath2.path.Path object>
>>> list(map(lambda match_data: match_data.current_value, p.match(d)))
[13]
>>> list(map(lambda match_data: match_data.node.tojsonpath(), p.match(d)))
['$["hello"][length()]']
```

The following functions are currently available:

* [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array):
  * [length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length): `length(): int`
  <!-- * concat -->
  * [entries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries): `entries(): List[Tuple[int, Any]]`
  <!-- * fill -->
  <!-- * flat -->
  <!-- * includes -->
  <!-- * indexOf -->
  <!-- * join -->
  * [keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/keys): `keys(): List[int]`
  <!-- * lastIndexOf -->
  <!-- * slice -->
  <!-- * sort -->
  <!-- * splice -->
  * [values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values): `values(): List[Any]`
<!-- * [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON): -->
  <!-- * parse -->
  <!-- * stringify -->
<!-- * [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math): -->
  <!-- * abs -->
  <!-- * acos -->
  <!-- * acosh -->
  <!-- * asin -->
  <!-- * asinh -->
  <!-- * atan -->
  <!-- * atan2 -->
  <!-- * atanh -->
  <!-- * cbrt -->
  <!-- * ceil -->
  <!-- * clz32 -->
  <!-- * cos -->
  <!-- * cosh -->
  <!-- * exp -->
  <!-- * expm1 -->
  <!-- * floor -->
  <!-- * fround -->
  <!-- * hypot -->
  <!-- * imul -->
  <!-- * log -->
  <!-- * log10 -->
  <!-- * log1p -->
  <!-- * log2 -->
  <!-- * max -->
  <!-- * min -->
  <!-- * pow -->
  <!-- * random -->
  <!-- * round -->
  <!-- * sign -->
  <!-- * sin -->
  <!-- * sinh -->
  <!-- * sqrt -->
  <!-- * tan -->
  <!-- * tanh -->
  <!-- * trunc -->
<!-- * [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number): -->
  <!-- * isFinite -->
  <!-- * isInteger -->
  <!-- * isNaN -->
  <!-- * isSafeInteger -->
  <!-- * parseFloat -->
  <!-- * parseInt -->
* [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object):
  * [entries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries): `entries(): List[Tuple[str, Any]]`
  * [keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) `keys(): List[str]`
  * [values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values) `values(): List[Any]`
* [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String):
  * [charAt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt): `charAt(index: int): str`
  <!-- * codeCharAt -->
  <!-- * codePointAt -->
  <!-- * concat -->
  <!-- * endsWith -->
  <!-- * includes -->
  <!-- * indexOf -->
  <!-- * lastIndexOf -->
  * [length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length): `length(): int`
  <!-- * localeCompare -->
  <!-- * match -->
  <!-- * normalize -->
  <!-- * padEnd -->
  <!-- * padStart -->
  <!-- * repeat -->
  <!-- * replace -->
  <!-- * search -->
  <!-- * slice -->
  <!-- * split -->
  <!-- * startsWith -->
  * [substring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring): `substring(indexStart: int, indexEnd: Optional[int]): str`
  <!-- * toLocaleLowerCase -->
  <!-- * toLocaleUpperCase -->
  <!-- * toLowerCase -->
  <!-- * toUpperCase -->
  <!-- * trim -->
  <!-- * trimEnd -->
  <!-- * trimStart -->

Type aliases (`Any`, `List`, `Optional` and `Tuple`) are defined by the [`typing`](https://docs.python.org/3/library/typing.html) module from the Python Standard Library.

## Grammar and parser

The [ANTLR v4](https://github.com/antlr/antlr4) grammar for JSONPath is available at `jsonpath2/parser/JSONPath.g4`.

### Installing ANTLR v4

Adapted from https://github.com/antlr/antlr4/blob/master/doc/getting-started.md.

```bash
cd /usr/local/lib
curl -O http://www.antlr.org/download/antlr-4.7.1-complete.jar

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'
```

### Building the parser for the grammar

Adapted from https://github.com/antlr/antlr4/blob/master/doc/python-target.md.

```bash
antlr4 -Dlanguage=Python3 -o . -lib . jsonpath2/parser/JSONPath.g4
```
