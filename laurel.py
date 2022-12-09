#! /usr/bin/env python3

from phaedriades import omphalos
from parnassus import *

import re
import sys

args = sys.argv
lyra = beadgcf


def fabricate():
    for sign in args:
        if omphalos.get(sign):
            print('')
            lyra(sign)
        else:
            print("\n\t{} ?".format(sign))
    print('')


def chalkboard():
    accum = str()
    count = 0
    for sign in sorted(omphalos.keys()):
        accum = accum + "\t{}".format(sign)
        count = count + 1
        if count % 7 == 0:
            accum = accum + "\n"

    print("\n{}\n".format(accum))
    print("Tunings:")
    print("\tbeadgcf bfbfb cgdae eadgbe fkbjdn\n")
    print("Example:")
    print("\tpython3 -B {} eadgbe n0 k6 j3 j6 j2\n".format(args[0]))


if len(args) > 1:
    dump = args.pop(0)
    head = args[0]

    if 'a4' in head:
        lyra = bfbfb
        dump = args.pop(0)
    elif 'adgb' in head:
        lyra = eadgbe
        dump = args.pop(0)
    elif 'bfb' in head:
        lyra = bfbfb
        dump = args.pop(0)
    elif 'cgda' in head:
        lyra = cgdae
        dump = args.pop(0)
    elif 'eadg' in head:
        lyra = beadgcf
        dump = args.pop(0)
    elif 'gdae' in head:
        lyra = cgdae
        dump = args.pop(0)
    elif 'fkbj' in head:
        lyra = fkbjdn
        dump = args.pop(0)
    elif 'p4' in head:
        lyra = beadgcf
        dump = args.pop(0)
    elif 'p5' in head:
        lyra = cgdae
        dump = args.pop(0)
    elif 'm3' in head:
        lyra = fkbjdn
        dump = args.pop(0)
    else:
        lyra = beadgcf

    if callable(lyra) and not len(args):
        print("\n\t {} [key [key [...]]]\n".format(dump))
    elif callable(lyra) and args[0] == 'gamut':
        pleistos(lyra)
    else:
        fabricate()

else:
    chalkboard()


