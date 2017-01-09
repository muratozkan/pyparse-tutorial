# retrieved from http://pyparsing.wikispaces.com/file/view/greeting.py/30112822/greeting.py

from pyparsing import Word, alphas, Suppress

# define grammar
greet = Word(alphas) + Suppress(",") + Word(alphas) + Suppress("!")

# input string
hello = "Hello, World!"

# parse input string
print(hello, "->", greet.parseString(hello).dump())
