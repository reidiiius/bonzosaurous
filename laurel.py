#! /usr/bin/env python3

"""Module laurel supplies interface routines to module parnassus."""

import sys
import os.path

from parnassus import *


def samples():
    """Interactive mode command examples."""
    mnemo = __name__
    stock = 'guitar'
    chart = "\t{}.fabricate({}, {})\n"
    lupus = "\t{} = {}.{}hound('{}')\n"
    tafel = "\t{}.chalkboard({})\n"
    trait = 'SnHg'
    if obtain('toggle'):
        trait = 'tv'

    batch = [
      "\n\t\t{}\n".format(mnemo.upper()),
      "\t{}.entryway()\n".format(mnemo),
      "\t{} = {}.eadgbe\n".format(stock, mnemo),
      chart.format(mnemo, stock, "['n0', 'k1']"),
      lupus.format('occurs', mnemo, 'grey', trait),
      tafel.format(mnemo, 'occurs'),
      lupus.format('occurs', mnemo, 'wolf', 'j3'),
      tafel.format(mnemo, 'occurs'),
      "\t{} = {}.refined()\n".format('traits', mnemo),
      tafel.format(mnemo, 'traits'),
      "\t{}.samples()\n".format(mnemo),
    ]
    for stout in batch:
        print(stout)

    return None


def tutorial():
    """Script mode menu and command examples."""
    quartet = "\t{} -B {} {} {}\n"
    sorcery = os.path.basename(sys.executable)
    profile = os.path.basename(sys.argv[0])
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
    """Application entry point."""
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


