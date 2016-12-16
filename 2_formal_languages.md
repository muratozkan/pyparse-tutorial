Formal Languages (Quick Recap)
==============================

Defined on a set of non-terminal and terminal symbols and a set of _production rules_.

Production Rules are used (not in specific order) to generate the set of string of symbols that defines the language.

_Samples_
- ab ba aa bb
- aaaaaaa...
- ababababab...
- ...

## Are all languages equal? 

Languages are classified by Noam Chomsky (1956) that is come to known as Chomsky Hierarchy

Regular < Context Free < Context Sensitive < Recursively Enumerable

Different grammars need different type of computer to be _recognized_

- Regular:                 Finite State Automaton
- Context Free:            Non-Deterministic Pushdown Automaton
- Context Sensitive:       Linear Bounded Non-Deterministic Turing Machine
- Recursively Enumerable:  Turing Machine

## What about Java?

*Java:* Context Free, but has static checks when parsing the type structure to rule out invalid combinations.

Next
----

Installing pyparsing