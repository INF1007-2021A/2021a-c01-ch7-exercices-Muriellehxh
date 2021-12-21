#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math

import re

# TODO: Définissez vos fonction ici
import turtle

from turtle import *

def draw_tree():
    setheading(90) # mettre ligne
    color("green") # color of line


    # partie récursive

    draw_branch(70, 7, 35)



    done() # dessin terminé

def draw_branch(branche_len, pen_size, angle ):  #BIEN RÉVISER
    # longueur branche réduit
    # largeur réduite
    # angle réduit + en plus

    speed(1)

    if branche_len > 0:
        pensize(pen_size)
        forward(branche_len)
        right(angle) #tourner un peu vers droite pour dessiner à droite
        draw_branch(branche_len - 10, pen_size - 1, angle - 2)

    # now, on doit aller vers la gauche pour dessiner 1ere branche (reculer)

        left(angle * 2)    # draw tree branch to the left
        draw_branch(branche_len - 10, pen_size - 1, angle - 2)

        right(angle)  #ramener branche vers milieu
        backward(branche_len)



def valide(sequence):


    # OU utiliser expression module (= simplifcation d'expression avec trucs comme '^', \, etc, LOOK UP ON INTERNET)

    # 1) import libraire re (voir en haut)
    # commence et continue uniquement actg du debut jusqua fin
    bool(re.match("^[actg]+$", sequence))


def saisie(type):
    value = input(f"{type}: ")

    if valide(value):
        return value
    # WE CANT PUT ELSE AFTER WE PUT RETURN IN IF

    print(f"La {type} n'est pas valide!")
    return saisie(type)




# TODO: Appelez vos fonctions ici





if __name__ == '__main__':

   # draw_tree()


   print(valide("agggaatttccc"))



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


print('\n Révision chap 7')


'Fonction récursives'


def factorielle(n):
    if n < 2:
        return 1
    else:
        return n * factorielle(n-1)


def naissance(nom_de_fichier):
    my_list = []

    dictionnaire_noms = {}

    with open("anniversaire.txt") as f:
        for ligne in f:
            my_list.append(ligne)
            print(my_list)

' LAMBDA FUNCTION INSIDE ANOTHER FUNCTION '

def quadratic_formula(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = (quadratic_formula(1, 4, 5))
print(f(2))

# OR

print(quadratic_formula(1, 4, 5)(2))

print(factorielle(4))


' Turtle recursive functions '
import turtle
stacy = turtle.Turtle()
stacy.goto(0, -100)
stacy.speed(1)

# def function
def draw_fractal( length, depth): # depth = how many lines it gets to
    stacy.forward(length)
    if depth > 1: # tell it to stop at one point
        stacy.backward(length/2) # cause she needs to go back halfway to cnter to draw other line
        stacy.left(90)
        # no drawinf new line yet!! we wait till we use recursion, so when we re-use little bit!!

        # stacy.forward(length/2.1)  <= instead we'll put recursive function so she repeats herself
        draw_fractal(length/2.1, depth - 1)  # length - 1 cause it'll never be less than one

        stacy.right(180)

        # stacy.forward(length/2.1)
        draw_fractal(length / 2.1, depth - 1)

        stacy.right(90)
        stacy.forward(length/2)

    stacy.right(180)
    stacy.forward(length)


# run function
# draw_fractal(200, 6)
# stacy.right(180)
# draw_fractal(200, 6)

#exit
#  turtle.exitonclick()