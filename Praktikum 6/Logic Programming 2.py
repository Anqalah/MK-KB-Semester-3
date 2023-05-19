# Nama  : Muhammad Fadhil
# NIM   : F55120068

from kanren import *
from kanren.core import lall

def left(q, p, list):
    return membero((q, p), zip(list, list[1:]))

def next(q, p, list):
    return conde([left(q, p, list)], [left(p, q, list)]);

houses = var()
zebraRules = lall(
    (eq, (var(), var(), var(), var(), var()), houses),
    # the Englishman's house is red
    (membero, ('Englishman', var(), var(), var(), 'red'), houses),
    # the Swede has a dog
    (membero, ('Swede', var(), var(), 'dog', var()), houses),
    # the Dane drinks tea
    (membero, ('Dane', var(), 'tea', var(), var()), houses),
    # the Green house is left of the White house
    (left, (var(), var(), var(), var(), 'green'),
     (var(), var(), var(), var(), 'white'), houses),
    # coffee is the drink of the green house
    (membero, (var(), var(), 'coffee', var(), 'green'), houses),
    # the Pall Mall smoker has birds
    (membero, (var(), 'Pall Mall', var(), 'birds', var()), houses),
    # the yellow house smokes Dunhills
    (membero, (var(), 'Dunhill', var(), var(), 'yellow'), houses),
    # the middle house drinks milk
    (eq, (var(), var(), (var(), var(), 'milk', var(), var()), var(), var()), houses),
    # the Norwegian is the first house
    (eq, (('Norwegian', var(), var(), var(), var()), var(), var(), var(), var()), houses),
    # the Blend smoker is in the house next to the house with cats
    (next, (var(), 'Blend', var(), var(), var()),
     (var(), var(), var(), 'cats', var()), houses),
    # the Dunhill smoker is next to the house where they have a horse
    (next, (var(), 'Dunhill', var(), var(), var()),
     (var(), var(), var(), 'horse', var()), houses),
    # the Blue Master smoker drinks beer
    (membero, (var(), 'Blue Master', 'beer', var(), var()), houses),
    # the German smokes Prince
    (membero, ('German', 'Prince', var(), var(), var()), houses),
    # the Norwegian is next to the blue house
    (next, ('Norwegian', var(), var(), var(), var()),
     (var(), var(), var(), var(), 'blue'), houses),
    # the house next to the Blend smoker drinks water
    (next, (var(), 'Blend', var(), var(), var()),
     (var(), var(), 'water', var(), var()), houses),
    # one of the houses has a zebra--but whose?
    (membero, (var(), var(), var(), 'zebra', var()), houses))

solusi = run(0, houses, zebraRules)

val = input("masukkan : ")
print(val)
output = [house for house in solusi[0] if val in house][0][0]
print('\n' + output + ' owns', val)