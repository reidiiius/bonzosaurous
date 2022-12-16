#! /usr/bin/env python3

from parnassus import *


class WhoDunit:
    def __init__(o, errata, passed, failed):
        o.errata = errata
        o.passed = passed
        o.failed = failed


    def logist(o, anomaly):
        straw = "\nanomaly[{}]: {}\n"
        o.errata.append(anomaly)
        return straw.format(o.failed, anomaly)


    def itemize(o):
        errors = tuple(enumerate(o.errata))
        return errors


    def summed(o):
        amount = int(o.passed + o.failed)
        return amount


    def __str__(o):
        straw = "Tested: {}, Passed: {}, Failed: {}"
        stats = straw.format(o.summed(), o.passed, o.failed)
        return stats


class VariCap(WhoDunit):
    def __init__(o, errata, passed, failed):
        WhoDunit.__init__(o, errata, passed, failed)


    def audition(o):
        print("\n{}".format(chr(45) * 53))
        if hasattr(o, 'errata') and len(o.errata):
            straw = "anomaly[{}]: {}"
            if callable(o.itemize):
                for numb, desc in o.itemize():
                    print(straw.format(numb + 1, desc))
            else:
                for desc in tuple(o.errata):
                    print(straw.format('?', desc))

        print("\n\t[ {} ]\n".format(o))
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

    for kind in (boards, metals, models):
        try:
            assert isinstance(kind, tuple), "instance Tuple"
            vc.passed += 1
        except Exception as anomaly:
            vc.failed += 1
            print(vc.logist(anomaly))

    for kind in (dyadic, stones):
        try:
            assert isinstance(kind, list), "instance List"
            vc.passed += 1
        except Exception as anomaly:
            vc.failed += 1
            print(vc.logist(anomaly))

    for kind in (chrono, resign, silent):
        try:
            assert isinstance(kind, str), "instance String"
            vc.passed += 1
        except Exception as anomaly:
            vc.failed += 1
            print(vc.logist(anomaly))

    try:
        assert isinstance(toggle, bool), "instance Boolean"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

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
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

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
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    bone = '56'
    try:
        assert isinstance(wolfhound(bone), list), "wolfhound returns List"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

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
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    desc = 'twine -> '
    for yarn in pegbox:
        try:
            assert len(yarn) == span, wiretap(desc + yarn, span)
            vc.passed += 1
        except Exception as anomaly:
            vc.failed += 1
            print(vc.logist(anomaly))

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
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    return None


def matrices(vc):
    sign = 'n0'
    cord = omphalos[sign]

    tuners = (
      beadgcf,
      bfbfb,
      cgdae,
      dadgad,
      dgdgbd,
      eadgbe,
      fkbjdn,
      unison,
    )

    for grid in tuners:
        try:
            assert grid(sign, cord) is None, "{} -> None".format(grid.__name__)
            vc.passed += 1
        except Exception as anomaly:
            vc.failed += 1
            print(vc.logist(anomaly))
        print('')

    return None


def sentinel(vc):
    sign = '0123456789ABCDEF'
    most = 10

    try:
        assert len(govern(sign)) <= most, "govern limit <= {}".format(most)
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    sign = 'j3k56m4'
    try:
        assert isinstance(validated(sign), bool), "validate returns Boolean"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    return None


def signatory(vc):
    stones = obtain('stones')

    lyra = fkbjdn
    try:
        assert fabricate(lyra, stones) is None, "fabricate returns None"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    lyra = beadgcf
    try:
        assert pleistos(lyra) is None, "pleistos returns None"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    try:
        assert chalkboard(stones) is None, "chalkboard returns None"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    return None


def scrutinize():
    vc = VariCap(list(), int(), int())

    desc = 'signatory test'
    print("\n\t\t{}".format(desc.upper()))
    signatory(vc)

    desc = 'sentinel test'
    print("\t\t{}\n".format(desc.upper()))
    sentinel(vc)

    desc = 'matrices test'
    print("\t\t{}\n".format(desc.upper()))
    matrices(vc)

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
    vc.audition()

    return None


if __name__ == '__main__':
    scrutinize()
else:
    print("\n\t\t{}".format(__name__.upper()))
    print("Sample:\n")
    print("\twhodunit.scrutinize()\n")


