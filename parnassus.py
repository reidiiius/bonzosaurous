#!/usr/bin/env python

from phaedriades import omphalos
import time

chronozoic = '-v' + str(time.time())

def Cello_P5(qp):
  print '\t' + qp + chronozoic
  print '\t' + omphalos[qp][20:60] + omphalos[qp][00:20] # En
  print '\t' + omphalos[qp][45:60] + omphalos[qp][00:45] # An
  print '\t' + omphalos[qp][10:60] + omphalos[qp][00:10] # Dn
  print '\t' + omphalos[qp][35:60] + omphalos[qp][00:35] # Gn
  print '\t' + omphalos[qp][00:60] + omphalos[qp][00:00] # Cn

def Guitar_P4(qp):
  print '\t' + qp + chronozoic
  print '\t' + omphalos[qp][25:60] + omphalos[qp][00:25] # Fn
  print '\t' + omphalos[qp][00:60] + omphalos[qp][00:00] # Cn
  print '\t' + omphalos[qp][35:60] + omphalos[qp][00:35] # Gn
  print '\t' + omphalos[qp][10:60] + omphalos[qp][00:10] # Dn
  print '\t' + omphalos[qp][45:60] + omphalos[qp][00:45] # An
  print '\t' + omphalos[qp][20:60] + omphalos[qp][00:20] # En
  print '\t' + omphalos[qp][55:60] + omphalos[qp][00:55] # Bn

def Guitar_Std(qp):
  print '\t' + qp + chronozoic
  print '\t' + omphalos[qp][20:60] + omphalos[qp][00:20] # En
  print '\t' + omphalos[qp][55:60] + omphalos[qp][00:55] # Bn
  print '\t' + omphalos[qp][35:60] + omphalos[qp][00:35] # Gn
  print '\t' + omphalos[qp][10:60] + omphalos[qp][00:10] # Dn
  print '\t' + omphalos[qp][45:60] + omphalos[qp][00:45] # An
  print '\t' + omphalos[qp][20:60] + omphalos[qp][00:20] # En

