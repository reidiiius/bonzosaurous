#!/usr/bin/env python

from time import time
from phaedriades import omphalos


baetylus = omphalos.keys()
baetylus.sort()

chronozoic = '-v' + str(time())


def Bj(qp):
    return omphalos[qp][50:] + omphalos[qp][:50]


def Fn(qp):
    return omphalos[qp][25:] + omphalos[qp][:25]


def Cn(qp):
    return omphalos[qp][:]


def Gn(qp):
    return omphalos[qp][35:] + omphalos[qp][:35]


def Dn(qp):
    return omphalos[qp][10:] + omphalos[qp][:10]


def An(qp):
    return omphalos[qp][45:] + omphalos[qp][:45]


def En(qp):
    return omphalos[qp][20:] + omphalos[qp][:20]


def Bn(qp):
    return omphalos[qp][55:] + omphalos[qp][:55]


def Fk(qp):
    return omphalos[qp][30:] + omphalos[qp][:30]


def beadgcf(qp):
    print "\t" + qp + '-beadgcf' + chronozoic
    print "\t" + Fn(qp)
    print "\t" + Cn(qp)
    print "\t" + Gn(qp)
    print "\t" + Dn(qp)
    print "\t" + An(qp)
    print "\t" + En(qp)
    print "\t" + Bn(qp)


def bfbfb(qp):
    print "\t" + qp + '-bfbfb' + chronozoic
    print "\t" + Bn(qp)
    print "\t" + Fn(qp)
    print "\t" + Bn(qp)
    print "\t" + Fn(qp)
    print "\t" + Bn(qp)


def cgdae(qp):
    print "\t" + qp + '-cgdae' + chronozoic
    print "\t" + En(qp)
    print "\t" + An(qp)
    print "\t" + Dn(qp)
    print "\t" + Gn(qp)
    print "\t" + Cn(qp)


def dadgad(qp):
    print "\t" + qp + '-dadgad' + chronozoic
    print "\t" + Dn(qp)
    print "\t" + An(qp)
    print "\t" + Gn(qp)
    print "\t" + Dn(qp)
    print "\t" + An(qp)
    print "\t" + Dn(qp)


def dgdgbd(qp):
    print "\t" + qp + '-dgdgbd' + chronozoic
    print "\t" + Dn(qp)
    print "\t" + Bn(qp)
    print "\t" + Gn(qp)
    print "\t" + Dn(qp)
    print "\t" + Gn(qp)
    print "\t" + Dn(qp)


def eadgbe(qp):
    print "\t" + qp + '-eadgbe' + chronozoic
    print "\t" + En(qp)
    print "\t" + Bn(qp)
    print "\t" + Gn(qp)
    print "\t" + Dn(qp)
    print "\t" + An(qp)
    print "\t" + En(qp)


def fkbjdn(qp):
    print "\t" + qp + '-fkbjdn' + chronozoic
    print "\t" + Dn(qp)
    print "\t" + Bj(qp)
    print "\t" + Fk(qp)
    print "\t" + Dn(qp)
    print "\t" + Bj(qp)
    print "\t" + Fk(qp)


def pleistos(lyra=eadgbe):
    print
    for qp in baetylus:
        print
        lyra(qp)
        print
    print


