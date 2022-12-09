#! /usr/bin/env python3

from phaedriades import omphalos
from parnassus import *

import re
import sys
import os.path


args = sys.argv

lyra = beadgcf

pate = re.compile('^([ijkn]+\d+)+([lm]\d+)?h?$', re.I)


def validated(sign):
  flag = pate.match(sign) and omphalos.get(sign)
  return flag


def fabricate():
    for sign in args:
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
    for sign in baetylus:
        accum = accum + "\t{}".format(sign)
        count = count + 1
        if count % 7 == 0:
            accum = accum + "\n"

    print("\n{}\n".format(accum))
    print("Tunings:")
    print("\tbeadgcf bfbfb cgdae eadgbe fkbjdn\n")
    print("Example:")
    print("\t{} -B {} eadgbe n0 k6 j3 j6 j2\n".format(named, args[0]))


if len(args) > 1:
    hold = args.pop(0)
    head = args[0]

    if 'a4' in head:
        lyra = bfbfb
        hold = args.pop(0)
    elif 'adgb' in head:
        lyra = eadgbe
        hold = args.pop(0)
    elif 'bfb' in head:
        lyra = bfbfb
        hold = args.pop(0)
    elif 'cgda' in head:
        lyra = cgdae
        hold = args.pop(0)
    elif 'dadg' in head:
        lyra = dadgad
        hold = args.pop(0)
    elif 'dgdg' in head:
        lyra = dgdgbd
        hold = args.pop(0)
    elif 'eadg' in head:
        lyra = beadgcf
        hold = args.pop(0)
    elif 'fkbj' in head:
        lyra = fkbjdn
        hold = args.pop(0)
    elif 'gdae' in head:
        lyra = cgdae
        hold = args.pop(0)
    elif 'm3' in head:
        lyra = fkbjdn
        hold = args.pop(0)
    elif 'p4' in head:
        lyra = beadgcf
        hold = args.pop(0)
    elif 'p5' in head:
        lyra = cgdae
        hold = args.pop(0)
    else:
        lyra = beadgcf

    if callable(lyra) and not len(args):
        print("\n\t {} key [key [...]]\n".format(hold))
    elif callable(lyra) and args[0] == 'gamut':
        pleistos(lyra)
    else:
        fabricate()

else:
    chalkboard()


