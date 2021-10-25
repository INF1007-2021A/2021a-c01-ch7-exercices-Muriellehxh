#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici


def total(a, b, c, masse_volumique):
    valeur_volume = 4 / 3 * math.pi * a * b * c
    masse = valeur_volume * masse_volumique
    print(valeur_volume, masse)



'écrivez un programme qui trie les lettres à partir du dictionnaire ' \
'et qui retourne la lettre avec la fréquence la plus haute, en utilisant ' \
'une fonction lambda (fichier chap 6 RENOMMEZ FICHIER CHAP 6)'
def tri_lettre(phrase):
    from ex_chap6 import frequence

    highest_frequency = (lambda max_value: max_value[0])((frequence(phrase)))
    return highest_frequency



# TODO: Appelez vos fonctions ici


total(2, 5, 7, 0.2)
phrase = 'I chime in with a havent you people ever heard of closing the goddamn door'






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



List_lines = ['Benjamin, 12 janvier 1982, Homme'], ['Marie, 27 septembre 1986, Femme']

dictionnaire_noms = {}
length_to_split = [1, 3, 1]



for ligne in List_lines:
    liste_personne = ligne[0].split(',')
    date_naissance = liste_personne[1].split()
    dictionnaire_ligne = {liste_personne[0]: date_naissance[2]}
    dictionnaire_noms.update(dictionnaire_ligne)

print(dictionnaire_noms)


def naissance(nom_de_fichier):
    my_list = []

    dictionnaire_noms = {}

    with open("anniversaire.txt") as f:
        for ligne in f:
            my_list.append(ligne)
            print(my_list)



