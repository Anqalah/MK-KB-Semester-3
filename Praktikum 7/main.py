from kanren import *
from kanren.core import lall

def left(q, p, list_data) :
    return membero((q, p), zip(list_data, list_data[1:]))

def next(q, p, list_data) :
    return conde([left(q, p, list_data)], [left(p, q, list_data)])

house = var()

rules_zebraproblem = lall((var(), var(), var(), var(), var()), houses),
(membero, ('Englishman', var(), var(), var(), 'red'), houses),
(membero, ('Swede', var(), var(), 'dog', var()), houses),
(membero, ('Dane', var(), 'tea', var(), var(), houses),
(membero, (left, (var(), var(), var(), var(), 'green'), (var(), var(), var(), 'white'), houses)
(membero))
 )
