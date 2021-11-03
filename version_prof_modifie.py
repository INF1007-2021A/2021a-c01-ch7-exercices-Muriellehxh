#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys
sys.path.insert(0, '/Users/kegaub_book/Documents/charge_cours/INF1007/20213/exercices/2021A_C01_ch6_1_exercices')
from exercice_ch6 import frequence
from turtle import *
import re


def compute_volume_and_mass(a=2, b=4, c=6, masse_vol=10):
    volume = math.pi * a * b * c * 4 / 3
    masse = volume * masse_vol

    return volume, masse



def valide(saisie):

    if len(saisie) != 0:
        return set(saisie).issubset("atgc")

    return False


def saisie(type):
    value = input(f"Entrez une {type} d'ADN valide: ")

    if valide(value):
        return value

    print(f"La {type} n'est pas valide")
    return saisie(type)


def proportion(chain, sequence):

    return chain.count(sequence) / len(chain)


def check_dna():
    chain = saisie("chaine")
    sequence = saisie("sequence")

    prop = proportion(chain, sequence)
    print("Il y a {0:.2f} % de {1}.".format(prop*100, sequence))


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(compute_volume_and_mass())
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("big big test bb"))
    check_dna()

