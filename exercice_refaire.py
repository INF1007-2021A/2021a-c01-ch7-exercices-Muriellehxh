#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math

import turtle

# TODO: Définissez vos fonction ici


def total(a, b, c, mv):
    V = 4/3 * math.pi * a * b * c
    M = V * mv
    return (V, M)


from exercice_ch6 import frequence   # we put a global statement for dict frequency, so that we can use it in a different file
# OR we couldve put import * to get global thing??

lettre_frequence = (lambda dictionary : max(dictionary, key=dictionary.get))  # get max item of dictionary with dictionary.get


def turtle_drawing(saisie):
    silly = turtle.Turtle()

    silly.forward(20)
    turtle.done()


def valide(saisie):
     if len(saisie) != 0:
        if set(saisie).issubset('atgc'):
            return True

     return False

def renvoie_chaine(saisie):
    if valide(saisie) is True:
        saisie_string = ([ch for ch in saisie])
        print(saisie_string)

def proportion(chaine, sequence)


if __name__ == '__main__':
    print(total(2, 4, 7, 0.2))

    print(lettre_frequence(frequence('soy une phrase')))

    # turtle_drawing()

    saisie = str(input('Écrire une chaine valide:'))
    print(renvoie_chaine(saisie))
