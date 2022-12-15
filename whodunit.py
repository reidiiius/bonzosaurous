#! /usr/bin/env python3

from sys import exc_info

from phaedriades import omphalos
from parnassus import *


class WhoDunit:
    def __init__(o, errata, passed, failed):
        o.errata = errata
        o.passed = passed
        o.failed = failed


    def __str__(o):
        stats = "Passed: {}, Failed: {}".format(o.passed, o.failed)
        return stats


class VariCap(WhoDunit):
    def __init__(o, errata, passed, failed):
        WhoDunit.__init__(o, errata, passed, failed)


    def itemize(o):
        errors = tuple(enumerate(o.errata))
        return errors


    def summed(o):
        amount = int(o.passed + o.failed)
        return amount


def audition(vc):
    print("\n{}".format(chr(45) * 53))
    if len(vc.errata):
        for numb, desc in vc.itemize():
            print("anomaly[{}]: {}".format(numb+1, desc))

    print("\n\t[ Tested: {}, {} ]\n".format(vc.summed(), vc))
    return None


def logist(arrows, amount):
    gnosis = exc_info()
    arrows.append(gnosis[1])
    print("\nanomaly[{}]: {}\n".format(amount, gnosis[1]))
    return None


def wiretap(word, numb):
    stout = "{} length {}".format(word, numb)
    return stout


def databank(vc):
    boards = obtain('boards')
    chrono = obtain('chrono')
    dyadic = obtain('dyadic')
    metals = obtain('metals')
    models = obtain('models')
    resign = obtain('resign')
    silent = obtain('silent')
    stones = obtain('stones')
    toggle = obtain('toggle')

    try:
        assert isinstance(boards, tuple), "boards instance Tuple"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(chrono, str), "chrono instance String"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(dyadic, list), "dyadic instance List"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(metals, tuple), "metals instance Tuple"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(models, tuple), "models instance Tuple"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(resign, str), "resign instance String"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(silent, str), "silent instance String"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(stones, list), "stones instance List"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(toggle, bool), "toggle instance Boolean"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert chalkboard(stones) is None, "chalkboard returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    return None


def polygraph(vc):
    toggle = obtain('toggle')

    sign = 'k1'
    cord = omphalos[sign]

    name = 'transit'
    span = 0

    # flip-flop
    if toggle:
        span = 36
    else:
        span = 60

    try:
        assert len(transit(cord)) is span, wiretap(name, span)
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    return None


def laelaps(vc):
    toggle = obtain('toggle')
    bone = None

    # flip-flop
    if toggle:
        bone = 'vu'
    else:
        bone = 'HgAu'

    try:
        assert isinstance(greyhound(bone), list), "greyhound returns List"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    bone = '56'
    try:
        assert isinstance(wolfhound(bone), list), "wolfhound returns List"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    return None


def pitchfork(vc):
    toggle = obtain('toggle')

    sign = 'j3'
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

    span = 0
    gear = 30
    wire = machine(cord, gear)

    # flip-flop
    if toggle:
        span = 38
    else:
        span = 64

    desc = 'machine -> '
    try:
        assert len(wire) == span, wiretap(desc + wire, span)
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    desc = 'twine -> '
    for yarn in pegbox:
        try:
            assert len(yarn) == span, wiretap(desc + yarn, span)
            vc.passed += 1
        except:
            vc.failed += 1
            logist(vc.errata, vc.failed)

    return None


def screenplay(vc):
    boards = obtain('boards')
    tuning = boards[0]

    sign = 'n0'
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

    try:
        assert layout(sign, tuning, pegbox) is None, "layout returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    return None


def instrument(vc):
    sign = 'j3k56m4'
    cord = omphalos[sign]

    try:
        assert beadgcf(sign, cord) is None, "beadgcf returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    print('')
    try:
        assert bfbfb(sign, cord) is None, "bfbfb returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    print('')
    try:
        assert cgdae(sign, cord) is None, "cgdae returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    print('')
    try:
        assert dadgad(sign, cord) is None, "dadgad returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    print('')
    try:
        assert dgdgbd(sign, cord) is None, "dgdgbd returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    print('')
    try:
        assert eadgbe(sign, cord) is None, "eadgbe returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    print('')
    try:
        assert fkbjdn(sign, cord) is None, "fkbjdn returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    print('')
    try:
        assert unison(sign, cord) is None, "unison returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    return None


def sentinel(vc):
    sign = 'j3k56m4'
    most = 10

    try:
        assert len(govern(sign)) <= most, "govern limit <= {}".format(most)
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    try:
        assert isinstance(validated(sign), bool), "validate returns Boolean"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    return None


def signatory(vc):
    stones = obtain('stones')
    lyra = fkbjdn

    try:
        assert fabricate(lyra, stones) is None, "fabricate returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    lyra = beadgcf
    try:
        assert pleistos(lyra) is None, "pleistos returns None"
        vc.passed += 1
    except:
        vc.failed += 1
        logist(vc.errata, vc.failed)

    return None


def scrutinize():
    vc = VariCap(list(), int(), int())

    desc = 'signatory test'
    print("\n\t\t{}".format(desc.upper()))
    signatory(vc)

    desc = 'sentinel test'
    print("\t\t{}\n".format(desc.upper()))
    sentinel(vc)

    desc = 'instrument test'
    print("\t\t{}\n".format(desc.upper()))
    instrument(vc)

    desc = 'screenplay test'
    print("\n\t\t{}\n".format(desc.upper()))
    screenplay(vc)

    desc = 'pitchfork test'
    print("\n\t\t{}".format(desc.upper()))
    pitchfork(vc)

    desc = 'laelaps test'
    print("\n\t\t{}".format(desc.upper()))
    laelaps(vc)

    desc = 'polygraph test'
    print("\n\t\t{}".format(desc.upper()))
    polygraph(vc)

    desc = 'databank test'
    print("\n\t\t{}".format(desc.upper()))
    databank(vc)

    # printout results
    audition(vc)

    return None


scrutinize()


