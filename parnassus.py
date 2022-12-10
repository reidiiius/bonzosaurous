#! /usr/bin/env python3

from time import time
from phaedriades import omphalos


def obtain(item='toggle'):
    bank = dict(
      stones = sorted(omphalos.keys()),
      chrono = '-v' + str(time()),
      toggle = True,
    )
    return bank[item]


def transit(cord):
    mets = ['__','Ti','Mn','Fe','Cu','Ag','Sn','Au','Hg','Pb','Ur','Np','Pu']
    alps = ['_', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    if obtain('toggle'):
        wire = str(cord)
        for old, new in zip(mets, alps):
            wire = wire.replace(old, new)
        return wire
    else:
        return cord


def Bj(sign):
    return transit(omphalos[sign][50:] + omphalos[sign][:50])


def Fn(sign):
    return transit(omphalos[sign][25:] + omphalos[sign][:25])


def Cn(sign):
    return transit(omphalos[sign][:])


def Gn(sign):
    return transit(omphalos[sign][35:] + omphalos[sign][:35])


def Dn(sign):
    return transit(omphalos[sign][10:] + omphalos[sign][:10])


def An(sign):
    return transit(omphalos[sign][45:] + omphalos[sign][:45])


def En(sign):
    return transit(omphalos[sign][20:] + omphalos[sign][:20])


def Bn(sign):
    return transit(omphalos[sign][55:] + omphalos[sign][:55])


def Fk(sign):
    return transit(omphalos[sign][30:] + omphalos[sign][:30])


def layout(sign, tuned, pegbox):
    print("\t" + sign + '-' + tuned + obtain('chrono'))
    for ndx in range(0, len(pegbox)):
        print("\t" + pegbox[ndx])


def beadgcf(sign):
    tuned = 'beadgcf'
    pegbox = [
        Fn(sign),
        Cn(sign),
        Gn(sign),
        Dn(sign),
        An(sign),
        En(sign),
        Bn(sign),
    ]
    layout(sign, tuned, pegbox)


def bfbfb(sign):
    tuned = 'bfbfb'
    pegbox = [
        Bn(sign),
        Fn(sign),
        Bn(sign),
        Fn(sign),
        Bn(sign),
    ]
    layout(sign, tuned, pegbox)


def cgdae(sign):
    tuned = 'cgdae'
    pegbox = [
        En(sign),
        An(sign),
        Dn(sign),
        Gn(sign),
        Cn(sign),
    ]
    layout(sign, tuned, pegbox)


def dadgad(sign):
    tuned = 'dadgad'
    pegbox = [
        Dn(sign),
        An(sign),
        Gn(sign),
        Dn(sign),
        An(sign),
        Dn(sign),
    ]
    layout(sign, tuned, pegbox)


def dgdgbd(sign):
    tuned = 'dgdgbd'
    pegbox = [
        Dn(sign),
        Bn(sign),
        Gn(sign),
        Dn(sign),
        Gn(sign),
        Dn(sign),
    ]
    layout(sign, tuned, pegbox)


def eadgbe(sign):
    tuned = 'eadgbe'
    pegbox = [
        En(sign),
        Bn(sign),
        Gn(sign),
        Dn(sign),
        An(sign),
        En(sign),
    ]
    layout(sign, tuned, pegbox)


def fkbjdn(sign):
    tuned = 'fkbjdn'
    pegbox = [
        Dn(sign),
        Bj(sign),
        Fk(sign),
        Dn(sign),
        Bj(sign),
        Fk(sign),
    ]
    layout(sign, tuned, pegbox)


def unison(sign):
    tuned = 'unison'
    pegbox = [
        Cn(sign),
        Cn(sign),
    ]
    layout(sign, tuned, pegbox)


def pleistos(lyra=eadgbe):
    print('')
    for sign in obtain('stones'):
        print('')
        lyra(sign)
        print('')
    print('')


