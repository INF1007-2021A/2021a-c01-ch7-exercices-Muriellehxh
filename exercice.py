#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math

import re

# TODO: Définissez vos fonction ici


def total(a, b, c, masse_volumique):
    valeur_volume = 4 / 3 * math.pi * a * b * c
    masse = valeur_volume * masse_volumique
    print(valeur_volume, masse)


import exercice_ch6
import sys

sys.path.insert(0, "/exercice_ch6.py")
from exercice_ch6 import frequence

def tri_lettre(phrase):

    dict_freq = (frequence(phrase))

    list_n = []
    for n in range(len(dict_freq)):
        list_n.append(n)

    letter = (lambda max_value: max(max_value)(list_n))
    return letter






# TODO: Appelez vos fonctions ici

if __name__ == '__main__':

   total(4, 5, 1, 0.1)

   phrase = 'je suis en train decrire une phrase'
   tri_lettre(phrase)





'CHAPITRE 7'
print('EXPLICATIONS CHAPITRE 7')


def f(a, b):
    # a et b sont des entiers naturels non nuls
    if b == 1:
        return a
    return a + f(a, b - 1)



print(f(3, 5))


'Valeurs par défaut'


def tableMulti(base, debut, fin):
    print('Fragment de la table de multiplication par', base, ':')
    n = debut
    while n <= fin:
        print(n, 'x', base, '=', n * base)
        n = n + 1


tableMulti(12, 5, 15)


def ma_function(x=None):
    if x:
        print(x)
    else:
        print('rien')


ma_function('test')
ma_function()


'Fonction rappel'


def additionn(x, y):
    return x + y


def operation(x, y, f):
    return f(x, y)


'LAMBDA'


def f(x):
    return x * 2

# est équivalent à

g = lambda x: x * 2
multi = g(5)
print(multi)

' Lambda sert à simplifier pour pas mettre de fonction'


# Tri d’une liste suivant des règles spécifiques
noms = ["B De Leener", "J Cohen", "M Guy", "K Lapierre"]
print(sorted(noms))  # Tri simple sur les chaînes de caractère
sorted_noms = sorted(noms, key=lambda x: x[2])
print(sorted_noms)  # Tri avec les noms de famille


def ma_fonction(x, y=10, z=15):
    return x * y * z


if __name__ == '__main__':
    x = ma_fonction(0, z=2, y=4)
    print(x)

'Fonction récursives'


def factorielle(n): 2


'if n <= 1'
'return 1'
'else'
'return (n * factorielle(n - 1))'


# TODO : Vidéo chap 7

' QUAND ON RENCONTRE RETURN, fonction sarrete'

' EX: Fonction de rappel' \


def f(a, b):
    return a+b

def operation(x, y, f):
    return x + y + f

original_f = f(2,3)
print(operation(4, 5, original_f))


' Variables locales et globales '

# glob = ext , loc = int fonction
# fonction locals(variable) to see if variable is local or global

# 4 espaces:
  # interne = toutes fonctions de python


' Fonction récursive '

def getFactorial (n):
    if n<2:
        return 1
    else:
        return n * getFactorial(n-1)

print(getFactorial(4))