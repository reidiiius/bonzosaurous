#! /usr/bin/env python3

from sys import exc_info

from phaedriades import omphalos
from parnassus import *


def logist(arrows, amount):
    gnosis = exc_info()
    arrows.append(gnosis[1])
    print("\nanomaly[{}]: {}\n".format(amount, gnosis[1]))
    return None


def wiretap(word, numb):
    stout = "{} returns string length {}".format(word, numb)
    return stout


def scrutinize():
    sign = 'j3k56m4'
    cord = omphalos[sign]
    clefs = obtain('stones')
    span = 0
    bone = 'vu'
    name = 'transit'
    gear = 30
    tuning = 'beadgcf'
    pegbox = [
      Bj(cord),
      Fn(cord),
      Cn(cord),
      Gn(cord),
      Dn(cord),
      An(cord),
      En(cord),
      Bn(cord),
      Fk(cord),
    ]
    word = sign
    most = 10
    lyra = beadgcf
    arts = clefs
    errata = []
    passed = 0
    failed = 0

    try:
        assert type(obtain('toggle')) is type(bool()), "obtain('toggle') Boolean"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    # flip-flop
    if obtain('toggle'):
        span = 36
    else:
        span = 60

    try:
        assert chalkboard(clefs) is None, "chalkboard returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert len(transit(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert type(greyhound(bone)) is type(list()), "greyhound returns List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    bone = '56'
    try:
        assert type(wolfhound(bone)) is type(list()), "wolfhound returns List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    # flip-flop
    if obtain('toggle'):
        span = 38
    else:
        span = 64

    name = 'machine'
    try:
        assert len(machine(cord, gear)) is span, wiretap(name, span) 
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'Bj'
    try:
        assert len(Bj(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'Fn'
    try:
        assert len(Fn(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'Cn'
    try:
        assert len(Cn(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'Gn'
    try:
        assert len(Gn(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'Dn'
    try:
        assert len(Dn(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'An'
    try:
        assert len(An(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'En'
    try:
        assert len(En(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'Bn'
    try:
        assert len(Bn(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'Fk'
    try:
        assert len(Fk(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert layout(sign, tuning, pegbox) is None, "layout returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert beadgcf(sign, cord) is None, "beadgcf returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert bfbfb(sign, cord) is None, "bfbfb returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert cgdae(sign, cord) is None, "cgdae returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert dadgad(sign, cord) is None, "dadgad returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert dgdgbd(sign, cord) is None, "dgdgbd returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert eadgbe(sign, cord) is None, "eadgbe returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert fkbjdn(sign, cord) is None, "fkbjdn returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert unison(sign, cord) is None, "unison returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'govern'
    try:
        assert len(govern(word)) <= most, "{} limit <= {}".format(name, most)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert type(validated(sign)) is type(bool()), "validate returns Boolean"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert fabricate(lyra, arts) is None, "fabricate returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert pleistos(lyra) is None, "pleistos returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    print('-' * 46)
    if len(errata):
        for numb, desc in enumerate(errata):
            print("anomaly[{}]: {}".format(numb+1, desc))

    print("\n\t[ Passed: {}, Failed: {} ]\n".format(passed, failed))
    return None


scrutinize()


