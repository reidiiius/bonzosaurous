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
    arts = []
    if len(sys.argv) > len(obtain('stones')):
        print("Request denied!")
        sys.exit(0)
    else:
      arts = sys.argv[0:]

    clave = 'i0'
    if bool(omphalos) and clave not in omphalos:
        omphalos[clave] = obtain('silent')

    if len(arts) > 1:
        lyra = beadgcf
        hold = govern(arts.pop(0))
        head = govern(arts[0])

        if 'group' in head and len(arts) > 1:
            bone = govern(arts[1])
            clefs = greyhound(bone)
            chalkboard(clefs)
            return None

        if 'query' in head and len(arts) > 1:
            bone = govern(arts[1])
            clefs = wolfhound(bone)
            chalkboard(clefs)
            return None

        if 'a4' in head:
            lyra = bfbfb
            hold = govern(arts.pop(0))
        elif 'adgb' in head:
            lyra = eadgbe
            hold = govern(arts.pop(0))
        elif 'bfb' in head:
            lyra = bfbfb
            hold = govern(arts.pop(0))
        elif 'cgda' in head:
            lyra = cgdae
            hold = govern(arts.pop(0))
        elif 'dadg' in head:
            lyra = dadgad
            hold = govern(arts.pop(0))
        elif 'dgdg' in head:
            lyra = dgdgbd
            hold = govern(arts.pop(0))
        elif 'eadg' in head:
            lyra = beadgcf
            hold = govern(arts.pop(0))
        elif 'fkbj' in head:
            lyra = fkbjdn
            hold = govern(arts.pop(0))
        elif 'gdae' in head:
            lyra = cgdae
            hold = govern(arts.pop(0))
        elif 'm3' in head:
            lyra = fkbjdn
            hold = govern(arts.pop(0))
        elif 'p4' in head:
            lyra = beadgcf
            hold = govern(arts.pop(0))
        elif 'p5' in head:
            lyra = cgdae
            hold = govern(arts.pop(0))
        elif 'un' in head:
            lyra = unison
            hold = govern(arts.pop(0))
        else:
            lyra = unison

        if callable(lyra) and not len(arts):
            print("\n\t {} key [key [...]]\n".format(hold))
        elif callable(lyra) and govern(arts[0]) == 'gamut':
            pleistos(lyra)
        else:
            fabricate(lyra, arts)

    else:
        clefs = obtain('stones')
        chalkboard(clefs)

    return None


entryway()


