# THE4 for Ceng111 in METU

This is 4th "take home exam" (THE) in 2022-2023 academic year.

## What is our task?:

In this THE, we will construct trees representing calculations as defined by a set of functions of
a fixed variable ‘x’. Function definitions will conform to the following rules:
<function-def> ==> <function> ’(’ <variable> ’)’ ‘=’ <term> <operator> <term>
<term> ==> <variable> | <constant> | <function> ’(’ <variable> ’)’
<function> ==> ’a’ | ’b’ | .. | ’z’ # excluding x
<variable> ==> ’x’
<constant> ==> ’1’ | ’2’ | .. | ’100’
<operator> ==> ’+’ | ’-’ | ’*’ | ’^’

#Sample Run:

>>> Defs = ["g(x   ) = x + 20", "h(x) = x * 100", "f(x) = g(x) * x"]
>>> Forest = construct_forest(Defs)
>>> print(Forest)
[[’f’, ’*’, [’g’, ’+’, [’x’], [’20’]], [’x’]], [’h’, ’*’, [’x’], [’100’]]]

## We are not allowed to:
– import any libraries

# Final result after gradeing:

This code got full score (100%)
