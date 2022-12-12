#! /usr/bin/env python3

import sys
import os.path

from phaedriades import omphalos
from parnassus import *


def tutorial():
    zithers = obtain('boards')
    attuned = chr(32).join(zithers)
    quartet = "\t{} -B {} {} {}\n"
    sorcery = os.path.basename(sys.executable)
    profile = sys.argv[0]
    instrum = zithers[5]
    signets = 'n0 k6 j3 j6'
    digraph = omphalos['j6'][0:4]

    if obtain('toggle'):
        digraph = transit(digraph)

    print("Tunings:")
    print("\t{}\n".format(attuned))
    print("Samples:")
    print(quartet.format(sorcery, profile, instrum, signets))
    print(quartet.format(sorcery, profile, 'group', digraph))
    print(quartet.format(sorcery, profile, 'query', '56'))

    return None


def entryway():
    arts = list()
    clef = 'i0'

    if len(sys.argv) > len(obtain('stones')):
        print("Request denied!")
        sys.exit(0)
    else:
        arts = sys.argv[1:]

    if bool(omphalos) and clef not in omphalos:
        omphalos[clef] = obtain('silent')

    if len(arts):
        head = govern(arts[0])
        lyra = None

        if head == 'group' and len(arts) > 1:
            bone = govern(arts[1])
            clefs = greyhound(bone)
            chalkboard(clefs)
            return None

        if head == 'query' and len(arts) > 1:
            bone = govern(arts[1])
            clefs = wolfhound(bone)
            chalkboard(clefs)
            return None

        if   head == 'beadgcf': lyra = beadgcf
        elif head == 'bfbfb'  : lyra = bfbfb
        elif head == 'cgdae'  : lyra = cgdae
        elif head == 'dadgad' : lyra = dadgad
        elif head == 'dgdgbd' : lyra = dgdgbd
        elif head == 'eadgbe' : lyra = eadgbe
        elif head == 'fkbjdn' : lyra = fkbjdn
        else                  : lyra = unison

        sign = str()
        flag = False
        for word in arts:
            sign = govern(word)
            if sign == 'gamut': flag = True

        if flag: pleistos(lyra)
        elif head == lyra.__name__:
            hold = arts.pop(0)
            if len(arts):
                fabricate(lyra, arts)
            else:
                clefs = obtain('stones')
                chalkboard(clefs)
        else:
            fabricate(lyra, arts)

    else:
        clefs = obtain('stones')
        chalkboard(clefs)
        if len(sys.argv) == 1:
            tutorial()

    return None


entryway()


