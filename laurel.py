#! /usr/bin/env python3

from phaedriades import omphalos
from parnassus import *

import re
import sys
import os.path


def validated(sign):
  most = len(sign) < 10
  spat = re.compile('^([ijkn]+\d+)+([lm]\d+)?h?$', re.I)
  flag = most and spat.match(sign) and sign in omphalos
  return flag


def fabricate(lyra):
    for sign in sys.argv:
        if validated(sign):
            print('')
            lyra(sign)
        else:
            print("\n\t{} ?".format(sign))
    print('')


def chalkboard():
    named = os.path.basename(sys.executable)
    accum = str()
    count = 0
    for sign in obtain('stones'):
        accum = accum + "\t{}".format(sign)
        count = count + 1
        if count % 7 == 0:
            accum = accum + "\n"

    print("\n{}\n".format(accum))
    print("Tunings:")
    print("\tbeadgcf bfbfb cgdae dadgad dgdgbd eadgbe fkbjdn\n")
    print("Example:")
    print("\t{} -B {} eadgbe n0 k6 j3 j6 j2\n".format(named, sys.argv[0]))


def entryway():
    if len(sys.argv) > len(obtain('stones')):
        print("Request denied!")
        sys.exit(0)

    if len(sys.argv) > 1:
        lyra = beadgcf
        hold = sys.argv.pop(0)
        head = sys.argv[0]

        if 'a4' in head:
            lyra = bfbfb
            hold = sys.argv.pop(0)
        elif 'adgb' in head:
            lyra = eadgbe
            hold = sys.argv.pop(0)
        elif 'bfb' in head:
            lyra = bfbfb
            hold = sys.argv.pop(0)
        elif 'cgda' in head:
            lyra = cgdae
            hold = sys.argv.pop(0)
        elif 'dadg' in head:
            lyra = dadgad
            hold = sys.argv.pop(0)
        elif 'dgdg' in head:
            lyra = dgdgbd
            hold = sys.argv.pop(0)
        elif 'eadg' in head:
            lyra = beadgcf
            hold = sys.argv.pop(0)
        elif 'fkbj' in head:
            lyra = fkbjdn
            hold = sys.argv.pop(0)
        elif 'gdae' in head:
            lyra = cgdae
            hold = sys.argv.pop(0)
        elif 'm3' in head:
            lyra = fkbjdn
            hold = sys.argv.pop(0)
        elif 'p4' in head:
            lyra = beadgcf
            hold = sys.argv.pop(0)
        elif 'p5' in head:
            lyra = cgdae
            hold = sys.argv.pop(0)
        elif 'un' in head:
            lyra = unison
            hold = sys.argv.pop(0)
        else:
            lyra = unison

        if callable(lyra) and not len(sys.argv):
            print("\n\t {} key [key [...]]\n".format(hold))
        elif callable(lyra) and sys.argv[0] == 'gamut':
            pleistos(lyra)
        else:
            fabricate(lyra)

    else:
        chalkboard()


entryway()


