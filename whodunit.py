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
    errata = []
    passed = 0
    failed = 0

    # compose umbworld
    boards = obtain('boards')
    tuning = boards[0]

    chrono = obtain('chrono')
    dyadic = obtain('dyadic')
    metals = obtain('metals')
    models = obtain('models')
    resign = obtain('resign')
    silent = obtain('silent')
    stones = obtain('stones')
    toggle = obtain('toggle')

    sign = 'j3k56m4'
    cord = omphalos[sign]
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

    bone = 'initiate'
    gear = 30
    lyra = beadgcf
    most = 10
    name = 'initiate'
    span = 0

    # flip-flop
    if toggle:
        bone = 'vu'
        span = 36
    else:
        bone = 'HgAu'
        span = 60

    try:
        assert isinstance(boards, list), "boards instance List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(chrono, str), "chrono instance String"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(dyadic, list), "dyadic instance List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(metals, list), "metals instance List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(models, list), "models instance List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(resign, str), "resign instance String"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(silent, str), "silent instance String"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(stones, list), "stones instance List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(toggle, bool), "toggle instance Boolean"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert chalkboard(stones) is None, "chalkboard returns None"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    name = 'transit'
    try:
        assert len(transit(cord)) is span, wiretap(name, span)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(greyhound(bone), list), "greyhound returns List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    bone = '56'
    try:
        assert isinstance(wolfhound(bone), list), "wolfhound returns List"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    # flip-flop
    if toggle:
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
        assert len(govern(sign)) <= most, "{} limit <= {}".format(name, most)
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert isinstance(validated(sign), bool), "validate returns Boolean"
        passed += 1
    except:
        failed += 1
        logist(errata, failed)

    try:
        assert fabricate(lyra, stones) is None, "fabricate returns None"
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

    print(chr(45) * 46)
    if len(errata):
        for numb, desc in enumerate(errata):
            print("anomaly[{}]: {}".format(numb+1, desc))

    print("\n\t[ Passed: {}, Failed: {} ]\n".format(passed, failed))
    return None


scrutinize()


