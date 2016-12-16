from pyparsing import Keyword, Word, infixNotation, opAssoc

# <constant> ::= False | True
# <variable> ::= 'p' | 'q' | 'r'
# <or> ::= 'or'
# <and> ::= 'and'
# <not> ::= 'not'
# <expression> ::= <term> { <or><term> }
# <term> ::= <factor> { <and><factor> }
# <factor> ::= <constant> | <not><factor> | (<expression>)


constant = Keyword('True') | Keyword('False')
variable = Word('pqr', exact=1)
operand = constant | variable

expr = infixNotation(operand, [
    ("not", 1, opAssoc.RIGHT, ),
    ("and", 2, opAssoc.LEFT, ),
    ("or",  2, opAssoc.LEFT, ),
])

test_strings = [
    'True',
    'not True',
    'p',
    'q and r',
    '(q and r)',
    '(False)',
    '(p and True)',
    '(p and q) or p',
    '(p and (not q or r)) or p',
]

for test in test_strings:
    print(expr.parseString(test))


# l_par, r_par = Suppress('('), Suppress(')')
#
# and_op = Keyword('and')
# or_op = Keyword('or')
# not_op = Keyword('not')
# variable = Word('pqr', exact=1)
# constant = Keyword('True') | Keyword('False')
#
# expr = Forward()
# factor = Forward()
# factor <<= constant | variable | Group(not_op + factor) | Group(l_par + expr + r_par)
# term = factor + ZeroOrMore(and_op + factor)
# expr <<= term + ZeroOrMore(or_op + factor)
