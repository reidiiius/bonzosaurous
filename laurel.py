#! /usr/bin/env python3

from phaedriades import omphalos
from parnassus import *

import re
import sys
import os.path


def govern(word):
    most = 10
    if len(word) > most:
        word = word[0:most]

    return word


def validated(sign):
  spat = re.compile('^([ijkn]+\d+)+([lm]\d+)?h?$', re.I)
  flag = spat.match(sign) and sign in omphalos
  return flag


def fabricate(lyra, arts):
    sign = str()
    for word in arts:
        sign = govern(word)
        if validated(sign):
            print('')
            lyra(sign)
        else:
            print("\n\t{} ?".format(sign))
    print('')
    return None


def chalkboard(clefs):
    named = os.path.basename(sys.executable)
    accum = str()
    count = 0
    for sign in clefs:
        accum = accum + "\t{}".format(sign)
        count = count + 1
        if count % 7 == 0:
            accum = accum + "\n"

    print("\n{}".format(accum))
    if count % 7 != 0: print('')

    if len(sys.argv) == 1:
        print("Tunings:")
        print("\tbeadgcf bfbfb cgdae dadgad dgdgbd eadgbe fkbjdn\n")
        print("Example:")
        print("\t{} -B {} eadgbe n0 k6 j3 j6 j2\n".format(named, sys.argv[0]))

    return None


def greyhound(bone):
    sack = list()
    for (clef, cord) in obtain('couple'):
        if obtain('toggle'):
            cord = transit(cord)

        if bone in cord:
            sack.append(clef)

    if len(sack) == 0:
        sack.append("{} ?".format(bone))

    return sack


def wolfhound(bone):
    sack = list()
    for clef in obtain('stones'):
        if bone in clef:
            sack.append(clef)

    if len(sack) == 0:
        sack.append("{} ?".format(bone))

    return sack


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


