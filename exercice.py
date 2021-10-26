#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici


def total(a, b, c, masse_volumique):
    valeur_volume = 4 / 3 * math.pi * a * b * c
    masse = valeur_volume * masse_volumique
    print(valeur_volume, masse)


import ex_chap6
import sys

sys.path.insert(0, "/Users/muriellemardenli/Desktop/poly/INF1007/2021a-c01-ch7-exercices-Muriellehxh/ex_chap6.py")
from ex_chap6 import frequence

def tri_lettre(phrase):
    return phrase


from turtle import *

def draw_tree():
    setheading(90) # mettre ligne
    color("green") # color of line


    # partie récursive

    draw_branch(70, 7, 35)



    done() # dessin terminé

def draw_branch(branche_len, pen_size, angle ):
    # longueur branche réduit
    # largeur réduite
    # angle réduit + en plus

    if branche_len > 0:
        pensize(pen_size)
        forward(branche_len)
        right(angle) #ramener branche vers centre
        draw_branch(branche_len - 10, pen_size - 1, angle - 2)

    # now, on doit aller vers la gauche pour dessiner 1ere branche (reculer)

        left(angle * 2)    # draw tree branch to the left
        draw_branch(branche_len - 10, pen_size - 1, angle - 2)

        right(angle)  #ramener branche vers milieu
        backward(branche_len)



# TODO: Appelez vos fonctions ici

if __name__ == '__main__':

   total(4, 5, 1, 0.1)

   phrase = 'je suis en train decrire une phrase'
   letter = tri_lettre((lambda max_value: max(frequence(phrase), key=frequence(phrase).get))(phrase))
   print(letter)


   draw_tree()


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



