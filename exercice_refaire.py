#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle

from turtle import *

# TODO: Définissez vos fonction ici


def total(a, b, c, mv):
    V = 4/3 * math.pi * a * b * c
    M = V * mv
    return (V, M)


from exercice_ch6 import frequence   # we put a global statement for dict frequency, so that we can use it in a different file
# OR we couldve put import * to get global thing??

lettre_frequence = (lambda dictionary : max(dictionary, key=dictionary.get))  # get max item of dictionary with dictionary.get


def draw_tree():
    setheading(90) # mettre ligne
    color("green") # color of line
    turtle_drawing(70, 7, 35)

    done()

def turtle_drawing(length, width, angle):

    if length>0:
        pensize(width)
        forward(length)
        right(angle)
        turtle_drawing(length - 10, width - 1, angle - 2)

        left(angle * 2)  # draw tree branch to the left
        turtle_drawing(length - 10, width - 1, angle - 2)

        right(angle)  # ramener branche vers milieu
        backward(length)



def valide(saisie):
     if len(saisie) != 0:
        if set(saisie).issubset('acgt'):
            return True

     return False

def renvoie_chaine(saisie):
    if valide(saisie) is True:
        saisie_string = ([ch for ch in saisie])
        return saisie_string

def proportion(chaine, sequence):
    return chaine.count(sequence) / len(chaine)


if __name__ == '__main__':
    print(total(2, 4, 7, 0.2))

    print(lettre_frequence(frequence('soy une phrase')))

    draw_tree()

    saisie = str(input('Écrire une chaine valide:'))

    print(renvoie_chaine(saisie))
    print(proportion(saisie, input('Entrer une séquence: ')))
