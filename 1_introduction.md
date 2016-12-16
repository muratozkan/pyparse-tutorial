Parsing
=======

_Parsing or syntactic analysis is the process of analysing a string of symbols, either in natural language or in 
computer languages, conforming to the rules of a formal grammar._

[Wikipedia, Parsing](https://en.wikipedia.org/wiki/Parsing)

We use quite a bit of parsing every day:

 - JSON
 - XML/SOAP
 - browsing the web (HTML, js and CSS parsing)
 - compiling and running a computer program

## The Process

 Input > 
    **Lexical Analysis** > Tokens > 
        **Syntactic Analysis** > Parse Tree > 
            **Semantic Analysis** > Output

 - Lexical Analysis
 
    A *lexer* creates _tokens_ from a given input string. Tokens are valid elements in a given language.
    
    E.g. Boolean Expressions:
    
    Input String: "(p and q) or (not r)"
    Tokens: '(', 'p', 'and', 'q', 'or', 'not', 'r', ')' 

 - Syntactic Analysis
 
    A *parser* checks whether the tokens form a valid syntax w.r.t a formal grammar. Then it generates the 
    resulting parse tree. Usually, most rules can be expressed via a _Context Free Language_. 
    
    E.g. 
    
    Input String: "(p and q) or (not r)"
    Parse Tree: 
        Expression = (p and q) or (not r)
            Expression = (p and q)
                Variable = p
                Operation = and
                Variable = q
            Operation = or
            Expression = (not r)
                Operation = not
                Variable = r

 - Semantic Analysis
 
    Working out the parse tree for a specific purpose. 
    
    E.g. 
        Compiler: Creates an executable representation in a lower level language
        Web Browser: Visually create the page
        Boolean Expression: Evaluate the tree and return a result

Next
----

Formal Languages (Quick Recap)