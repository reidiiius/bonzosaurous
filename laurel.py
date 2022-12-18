#! /usr/bin/env python3

import sys
import os.path

from parnassus import *


def samples():
    trait = str()
    if obtain('toggle'):
        trait = 'tv'
    else:
        trait = 'SnHg'

    clerk = "\tlaurel.chalkboard({})\n"
    batch = [
      "\n\t\t{}\n".format(__name__.upper()),
      "\tlaurel.entryway()\n",
      "\tguitar = laurel.eadgbe\n",
      "\tlaurel.fabricate(guitar, ['n0', 'k1'])\n",
      "\toccurs = laurel.greyhound('{}')\n".format(trait),
      clerk.format('occurs'),
      "\toccurs = laurel.wolfhound('j3')\n",
      clerk.format('occurs'),
      "\ttraits = laurel.refined()\n",
      clerk.format('traits'),
      "\tlaurel.samples()\n",
    ]
    for stout in batch:
        print(stout)

    return None


def choices():
    zithers = obtain('boards')
    attuned = chr(32).join(zithers)
    print("\t{}\n".format(attuned))

    return None


def tutorial():
    quartet = "\t{} -B {} {} {}\n"
    sorcery = os.path.basename(sys.executable)
    profile = sys.argv[0]
    zithers = obtain('boards')
    instrum = zithers[5]
    signets = 'n0 k6 j3 j6'
    digraph = omphalos['j6'][0:4]

    if obtain('toggle'):
        digraph = transit(digraph)

    print("Tunings:")
    choices()
    print("Samples:")
    print(quartet.format(sorcery, profile, instrum, signets))
    print(quartet.format(sorcery, profile, 'group', digraph))
    print(quartet.format(sorcery, profile, 'query', '56'))
    print(quartet.format(sorcery, profile, 'tonal', str()))

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

        if head == 'tonal' and len(arts) == 1:
            tones = refined()
            chalkboard(tones)
            return None

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
            if __name__ == '__main__':
                tutorial()
            else:
                choices()

    return None


if __name__ == '__main__':
    entryway()
else:
    samples()


