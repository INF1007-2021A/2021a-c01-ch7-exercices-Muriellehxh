#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici


def total(a, b, c, masse_volumique):
    valeur_volume = 4 / 3 * math.pi * a * b * c
    masse = valeur_volume * masse_volumique
    print(valeur_volume, masse)


# TODO: Appelez vos fonctions ici


total(2, 5, 7, 0.2)

'CHAPITRE 7'
print('EXPLICATIONS CHAPITRE 7')


def f(a, b):
    # a et b sont des entiers naturels non nuls
    if b == 1:
        return a
    return a + f(a, b - 1)


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
    return x * 2


# est équivalent à

g = lambda x: x * 2
multi = g(5)
print(multi)

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


def latin_phrase_to_english(pig_latin_phrase):
    list_pig_latin_words = pig_latin_phrase.split()
    print(list_pig_latin_words)


latin_phrase_to_english('onStr sjncn dwdew')

for word, number in latin_phrase_to_english('onStr sync dwdew'):
    for letter in word:
        if letter == 'e':
            print(word)




    for number in vec:
        if number == min(vec):
            if number == -1:
                continue
            else:
                indice, minimum = vec[number], number
                return vec[number], number
    print(vec[number], number)

    dict_valeurs_minimales_noeud = {}
    second_dict = {}

    for list_noeud in matrice:

        for numb in noeuds_vis_fake:
            if list_noeud[numb] == -1:
                continue
            else:
                dict_valeurs_minimales_noeud = {matrice.index(list_noeud): list_noeud[numb]}
                second_dict.update(dict_valeurs_minimales_noeud)

    print(second_dict)

    noeud_arriver = min(second_dict, key=second_dict.get)

    # To do: utiliser la fonction noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)

    noeuds_vis_fake.remove(2)
    noeud_depart, poids_min = noeudMinimalNonVisitesDeNoeud(matrice, noeud_arriver, noeuds_vis_fake)
    return noeud_depart, noeud_arriver