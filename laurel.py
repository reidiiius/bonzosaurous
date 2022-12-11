#! /usr/bin/env python3

import sys
import os.path

from phaedriades import omphalos
from parnassus import *


def tutorial():
    zithers = obtain('boards')
    attuned = chr(32).join(zithers)
    sorcery = os.path.basename(sys.executable)
    profile = sys.argv[0]
    instrum = zithers[5]

    print("Tunings:")
    print("\t{}\n".format(attuned))
    print("Example:")
    print("\t{} -B {} {} n0 k6 j3 j6\n".format(sorcery, profile, instrum))
    return None


def chalkboard(clefs):
    accum = str()
    count = int()
    for sign in clefs:
        accum = accum + "\t{}".format(sign)
        count = count + 1
        if count % 7 == 0:
            accum = accum + "\n"

    print("\n{}".format(accum))
    if count % 7 != 0: print('')

    if len(sys.argv) == 1:
        tutorial()
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
    return None


entryway()


