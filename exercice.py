#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math






def total(a, b, c, masse_volumique):
    valeur_volume = 4/3 * math.pi * a * b * c
    masse = valeur_volume * masse_volumique
    print(valeur_volume, masse)

total(2, 5, 7, 0.2)



# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass



'CHAPITRE 7'
print('EXPLICATIONS CHAPITRE 7')


def f(a, b):
    # a et b sont des entiers naturels non nuls
    if b==1:
        return a
    return a + f(a, b-1)
print(f(3, 5))

'***ask teacher****'



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
   return x*2

# est équivalent à

g = lambda x: x*2
multi = g(5)
print(multi)


# Tri d’une liste suivant des règles spécifiques
noms = ["B De Leener", "J Cohen", "M Guy", "K Lapierre"]
print(sorted(noms)) # Tri simple sur les chaînes de caractère
sorted_noms = sorted(noms, key=lambda x: x[2])
print(sorted_noms) # Tri avec les noms de famille


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
