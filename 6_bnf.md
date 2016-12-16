Backus-Naur Form
================

_A notation technique for context-free grammars, often used to describe the syntax of languages used in computing, 
such as computer programming languages, document formats, instruction sets and communication protocols._

[Wikipedia, Backus-Naur form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)

    symbol ::= _expansion_

EBNF (*Extended Backus–Naur Form*) is a notation to express a _context-free grammar_ formally.

Sample Boolean Expression in EBNF

    <expression> ::= <term> { <or><term> }
    <term> ::= <factor> { <and><factor> }
    <factor> ::= <constant> | <not><factor> | (<expression>)
    <constant> ::= False | True
    <variable> ::= 'p' | 'q' | 'r' 
    <or> ::= 'or'
    <and> ::= 'and'
    <not> ::= 'not'
    
Sample expressions 

    True
    (False)
    p
    p and True
    (p and q) or (q and True)
    ((p and q) or r)

Next
----

Creating a parser from EBNF