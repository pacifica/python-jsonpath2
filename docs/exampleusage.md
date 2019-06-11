# Example Usage

The JSONPath2 library has several APIs available to perform JSONPath
matching.

## Syntax

```eval_rst
+--------+----------------------+-----------------------------------+
| XPath  | JSONPath             | Description                       |
+========+======================+===================================+
| ``/``  | ``$``                | the root JSON value               |
+--------+----------------------+-----------------------------------+
| ``.``  | ``@``                | the current JSON value            |
+--------+----------------------+-----------------------------------+
| ``/``  | ``.`` or ``[]``      | child operator                    |
+--------+----------------------+-----------------------------------+
| ``//`` | ``..``               | recursive descent (depth-first    |
|        |                      | search)                           |
+--------+----------------------+-----------------------------------+
| ``*``  | ``*``                | wildcard (all elements of a JSON  |
|        |                      | array; all values of a JSON       |
|        |                      | object; otherwise none)           |
+--------+----------------------+-----------------------------------+
| ``[]`` | ``[]``               | subscript operator                |
+--------+----------------------+-----------------------------------+
| ``|``  | ``[,]``              | union operator (for two or more   |
|        |                      | subscript operators)              |
+--------+----------------------+-----------------------------------+
| n/a    | ``[start:end:step]`` | slice operator (subset of         |
|        |                      | elements of a JSON array)         |
+--------+----------------------+-----------------------------------+
| ``[]`` | ``?()``              | filter expression (for use with   |
|        |                      | subscript operator)               |
+--------+----------------------+-----------------------------------+

+-------------------+-----------------------------------------------+
| JSONPath Filter   |  Description                                  |
| Expression        |                                               |
+===================+===============================================+
| ``$`` or ``@``    | nested JSONPath (returns ``true`` if any      |
|                   | match exists; otherwise, returns ``false``)   |
+-------------------+-----------------------------------------------+
| ``=``, ``!=``,    | binary operator, where left- and right-hand   |
| ``>=``, ``<=``    | operands are nested JSONPaths or JSON values  |
| ``>``, ``<``      | (returns ``true`` if any match exists;        |
|                   | otherwise, returns ``false``)                 |
+-------------------+-----------------------------------------------+
| ``and``, ``or``,  | Boolean operator, where operands are JSONPath |
| ``not``           | filter expressions                            |
+-------------------+-----------------------------------------------+
| ``(`` ... ``)``   | parentheses                                   |
+-------------------+-----------------------------------------------+
```

## Functions

> See [#14](https://github.com/pacifica/python-jsonpath2/pull/14) for more information.

The syntax for a function call is the name of the function followed by the
arguments in parentheses, i.e., `name(arg1, arg2, ..., argN)`, where the
arguments are either JSONPaths or JSON values.

```python
>>> s = '{"hello":"Hello, world!"}'
'{"hello":"Hello, world!"}'
>>> import json
>>> d = json.loads(s)
{'hello':'Hello, world!'}
>>> from jsonpath2.path import Path
>>> p = Path.parse_str('$["hello"][length()]')
<jsonpath2.path.Path object>
>>> [m.current_value for m in p.match(d)]
[13]
>>> [m.node.tojsonpath() for m in p.match(d)]
['$["hello"][length()]']
```

```eval_rst
+------------------------------+--------------------------------------+
| JavaScript Function          | Signature                            |
+==============================+======================================+
| Array.length_                | ``length(): int``                    |
+------------------------------+--------------------------------------+
| Array.prototype.entries_     | ``entries(): List[Tuple[int, Any]]`` |
+------------------------------+--------------------------------------+
| Array.prototype.keys_        | ``keys(): List[int]``                |
+------------------------------+--------------------------------------+
| Array.prototype.values_      | ``values(): List[Any]``              |
+------------------------------+--------------------------------------+
| Object.entries_              | ``entries(): List[Tuple[str, Any]]`` |
+------------------------------+--------------------------------------+
| Object.keys_                 | ``keys(): List[str]``                |
+------------------------------+--------------------------------------+
| Object.values_               | ``values(): List[Any]``              |
+------------------------------+--------------------------------------+
| String.length_               | ``length(): int``                    |
+------------------------------+--------------------------------------+
| String.prototype.charAt_     | ``charAt(index: int): str``          |
+------------------------------+--------------------------------------+
| String.prototype.substring_  | ``substring(indexStart: int,         |
|                              | indexEnd: Optional[int]): str``      |
+------------------------------+--------------------------------------+

.. _Array.length: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length
.. _Array.prototype.entries: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries
.. _Array.prototype.keys: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/keys
.. _Array.prototype.values: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values
.. _Object.entries: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
.. _Object.keys: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys
.. _Object.values: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values
.. _String.length: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length
.. _String.prototype.charAt: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt
.. _String.prototype.substring: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring
```
<!-- | `Array.prototype.concat()` | |
| `Array.prototype.fill()` | |
| `Array.prototype.flat()` | |
| `Array.prototype.includes()` | |
| `Array.prototype.indexOf()` | |
| `Array.prototype.join()` | |
| `Array.prototype.lastIndexOf()` | |
| `Array.prototype.slice()` | |
| `Array.prototype.sort()` | |
| `Array.prototype.splice()` | |
| `JSON.parse()` | |
| `JSON.stringify()` | |
| `Math.abs()` | |
| `Math.acos()` | |
| `Math.acosh()` | |
| `Math.asin()` | |
| `Math.asinh()` | |
| `Math.atan()` | |
| `Math.atan2()` | |
| `Math.atanh()` | |
| `Math.cbrt()` | |
| `Math.ceil()` | |
| `Math.clz32()` | |
| `Math.cos()` | |
| `Math.cosh()` | |
| `Math.exp()` | |
| `Math.expm1()` | |
| `Math.floor()` | |
| `Math.fround()` | |
| `Math.hypot()` | |
| `Math.imul()` | |
| `Math.log()` | |
| `Math.log10()` | |
| `Math.log1p()` | |
| `Math.log2()` | |
| `Math.max()` | |
| `Math.min()` | |
| `Math.pow()` | |
| `Math.random()` | |
| `Math.round()` | |
| `Math.sign()` | |
| `Math.sin()` | |
| `Math.sinh()` | |
| `Math.sqrt()` | |
| `Math.tan()` | |
| `Math.tanh()` | |
| `Math.trunc()` | |
| `Number.isFinite()` | |
| `Number.isInteger()` | |
| `Number.isNaN()` | |
| `Number.isSafeInteger()` | |
| `Number.parseFloat()` | |
| `Number.parseInt()` | |
| `String.prototype.codeCharAt()` | |
| `String.prototype.codePointAt()` | |
| `String.prototype.concat()` | |
| `String.prototype.endsWith()` | |
| `String.prototype.includes()` | |
| `String.prototype.indexOf()` | |
| `String.prototype.lastIndexOf()` | |
| `String.prototype.localeCompare()` | |
| `String.prototype.match()` | |
| `String.prototype.normalize()` | |
| `String.prototype.padEnd()` | |
| `String.prototype.padStart()` | |
| `String.prototype.repeat()` | |
| `String.prototype.replace()` | |
| `String.prototype.search()` | |
| `String.prototype.slice()` | |
| `String.prototype.split()` | |
| `String.prototype.startsWith()` | |
| `String.prototype.toLocaleLowerCase()` | |
| `String.prototype.toLocaleUpperCase()` | |
| `String.prototype.toLowerCase()` | |
| `String.prototype.toUpperCase()` | |
| `String.prototype.trim()` | |
| `String.prototype.trimEnd()` | |
| `String.prototype.trimStart()` | | -->

In the above table, the type aliases (`Any`, `List`, `Optional` and `Tuple`) are defined by the
[`typing`](https://docs.python.org/3/library/typing.html) module from the Python Standard Library.

## Examples

Some of the examples are provided by the test suite while some have been contributed via issues.

### Test Suite Examples

```eval_rst
.. automodule:: bookstore_test
   :members:
   :private-members:
   :special-members:
```

### Issue Examples

#### Issue #19

This issue involved finding the full path to the matched attribute.

The result isn't strictly supported by the library but code examples are provided.

```python
import json
import typing

from jsonpath2.node import Node
from jsonpath2.nodes.root import RootNode
from jsonpath2.nodes.subscript import SubscriptNode
from jsonpath2.nodes.terminal import TerminalNode
from jsonpath2.path import Path
from jsonpath2.subscript import Subscript

data = json.loads("""
{
    "values": [
        {"type": 1, "value": 2},
        {"type": 2, "value": 3},
        {"type": 1, "value": 10}
    ]
}
""")

path = Path.parse_str("$.values.*[?(@.type = 1)].value")

def get_subscripts(node: Node) -> typing.List[typing.List[Subscript]]:
    return get_subscripts_(node, [])

def get_subscripts_(node: Node, accumulator: typing.List[typing.List[Subscript]]) -> typing.List[typing.List[Subscript]]:
    if isinstance(node, RootNode):
        return get_subscripts_(node.next_node, accumulator)
    elif isinstance(node, SubscriptNode):
        accumulator.append(node.subscripts)
        return get_subscripts_(node.next_node, accumulator)
    elif isinstance(node, TerminalNode):
        return accumulator

for match_data in path.match(data):
    print(f"Value: {match_data.current_value}")
    print(f"JSONPath: {match_data.node.tojsonpath()}")
    print(f"Subscripts: {get_subscripts(match_data.node)}")
    print("")
```

The snippet above iterates over the match results, prints the value and
JSONPath and then prints the list of subscripts. The list of subscripts
is constructed by traversing the structure of the abstract syntax tree
for the JSONPath.

The results [modulo the memory addresses] are:

```
Value: 2
JSONPath: $["values"][0]["value"]
Subscripts: [[<jsonpath2.subscripts.objectindex.ObjectIndexSubscript object at 0x10f6a3278>], [<jsonpath2.subscripts.arrayindex.ArrayIndexSubscript object at 0x10f6a37b8>], [<jsonpath2.subscripts.objectindex.ObjectIndexSubscript object at 0x10f6a3390>]]

Value: 10
JSONPath: $["values"][2]["value"]
Subscripts: [[<jsonpath2.subscripts.objectindex.ObjectIndexSubscript object at 0x10f6a3278>], [<jsonpath2.subscripts.arrayindex.ArrayIndexSubscript object at 0x10f6a3978>], [<jsonpath2.subscripts.objectindex.ObjectIndexSubscript object at 0x10f6a3390>]]
```

The first subscript is the `"values"` key. The second subscript is the
index of the `{"type":"value"}` object. The third subscript is the
`"value"` key.

Note that the result (the list of subscripts) is a list of lists. This
is because instances of the `SubscriptNode` class are constructed using
zero or more instances of the `Subscript` class.

## Grammar and parser

The [ANTLR v4](https://github.com/antlr/antlr4) grammar for JSONPath is available at `jsonpath2/parser/JSONPath.g4`.

### Installing ANTLR v4

Adapted from [antlr docs](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md).

```bash
cd /usr/local/lib
curl -O http://www.antlr.org/download/antlr-4.7.1-complete.jar

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'
```

### Building the parser for the grammar

Adapted from [antlr docs](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

```bash
antlr4 -Dlanguage=Python3 -o . -lib . jsonpath2/parser/JSONPath.g4
```
