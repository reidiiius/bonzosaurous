#!/usr/bin/env python

from time import time
from phaedriades import omphalos


baetylus = sorted(omphalos.keys())

chronozoic = '-v' + str(time())


def Bj(sign):
    return omphalos[sign][50:] + omphalos[sign][:50]


def Fn(sign):
    return omphalos[sign][25:] + omphalos[sign][:25]


def Cn(sign):
    return omphalos[sign][:]


def Gn(sign):
    return omphalos[sign][35:] + omphalos[sign][:35]


def Dn(sign):
    return omphalos[sign][10:] + omphalos[sign][:10]


def An(sign):
    return omphalos[sign][45:] + omphalos[sign][:45]


def En(sign):
    return omphalos[sign][20:] + omphalos[sign][:20]


def Bn(sign):
    return omphalos[sign][55:] + omphalos[sign][:55]


def Fk(sign):
    return omphalos[sign][30:] + omphalos[sign][:30]


def beadgcf(sign):
    print("\t" + sign + '-beadgcf' + chronozoic)
    print("\t" + Fn(sign))
    print("\t" + Cn(sign))
    print("\t" + Gn(sign))
    print("\t" + Dn(sign))
    print("\t" + An(sign))
    print("\t" + En(sign))
    print("\t" + Bn(sign))


def bfbfb(sign):
    print("\t" + sign + '-bfbfb' + chronozoic)
    print("\t" + Bn(sign))
    print("\t" + Fn(sign))
    print("\t" + Bn(sign))
    print("\t" + Fn(sign))
    print("\t" + Bn(sign))


def cgdae(sign):
    print("\t" + sign + '-cgdae' + chronozoic)
    print("\t" + En(sign))
    print("\t" + An(sign))
    print("\t" + Dn(sign))
    print("\t" + Gn(sign))
    print("\t" + Cn(sign))


def dadgad(sign):
    print("\t" + sign + '-dadgad' + chronozoic)
    print("\t" + Dn(sign))
    print("\t" + An(sign))
    print("\t" + Gn(sign))
    print("\t" + Dn(sign))
    print("\t" + An(sign))
    print("\t" + Dn(sign))


def dgdgbd(sign):
    print("\t" + sign + '-dgdgbd' + chronozoic)
    print("\t" + Dn(sign))
    print("\t" + Bn(sign))
    print("\t" + Gn(sign))
    print("\t" + Dn(sign))
    print("\t" + Gn(sign))
    print("\t" + Dn(sign))


def eadgbe(sign):
    print("\t" + sign + '-eadgbe' + chronozoic)
    print("\t" + En(sign))
    print("\t" + Bn(sign))
    print("\t" + Gn(sign))
    print("\t" + Dn(sign))
    print("\t" + An(sign))
    print("\t" + En(sign))


def fkbjdn(sign):
    print("\t" + sign + '-fkbjdn' + chronozoic)
    print("\t" + Dn(sign))
    print("\t" + Bj(sign))
    print("\t" + Fk(sign))
    print("\t" + Dn(sign))
    print("\t" + Bj(sign))
    print("\t" + Fk(sign))


def pleistos(lyra=eadgbe):
    print('')
    for sign in baetylus:
        print('')
        lyra(sign)
        print('')
    print('')


