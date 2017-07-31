#!/usr/bin/env python

from phaedriades import omphalos
import time

chronozoic = '-v' + str(time.time())

def Bj(qp):
    return omphalos[qp][50:60] + omphalos[qp][00:50]

def Fn(qp):
    return omphalos[qp][25:60] + omphalos[qp][00:25]

def Cn(qp):
    return omphalos[qp][00:60]

def Gn(qp):
    return omphalos[qp][35:60] + omphalos[qp][00:35]

def Dn(qp):
    return omphalos[qp][10:60] + omphalos[qp][00:10]

def An(qp):
    return omphalos[qp][45:60] + omphalos[qp][00:45]

def En(qp):
    return omphalos[qp][20:60] + omphalos[qp][00:20]

def Bn(qp):
    return omphalos[qp][55:60] + omphalos[qp][00:55]

def Fk(qp):
    return omphalos[qp][30:60] + omphalos[qp][00:30]

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

