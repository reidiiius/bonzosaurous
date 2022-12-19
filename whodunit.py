#! /usr/bin/env python3

"""Module whodunit operates as a unit testing workbench."""

from parnassus import *


class WhoDunit:
    def __init__(self, errata, passed, failed):
        self.errata = errata
        self.passed = passed
        self.failed = failed


    def logist(self, anomaly):
        straw = "\nanomaly[{}]: {}\n"
        self.errata.append(anomaly)
        return straw.format(self.failed, anomaly)


    def itemize(self):
        errors = tuple(enumerate(self.errata))
        return errors


    def summed(self):
        amount = int(self.passed + self.failed)
        return amount


    def __str__(self):
        straw = "Tested: {}, Passed: {}, Failed: {}"
        stats = straw.format(self.summed(), self.passed, self.failed)
        return stats


class VariCap(WhoDunit):
    def __init__(self, errata, passed, failed):
        WhoDunit.__init__(self, errata, passed, failed)


    def audition(self):
        print("\n{}".format(chr(45) * 53))
        if hasattr(self, 'errata') and len(self.errata):
            straw = "anomaly[{}]: {}"
            if callable(self.itemize):
                for numb, desc in self.itemize():
                    print(straw.format(numb + 1, desc))
            else:
                for desc in tuple(self.errata):
                    print(straw.format('?', desc))

        print("\n\t[ {} ]\n".format(self))
        return None


def wiretap(word, numb):
    stout = "{} length {}".format(word, numb)
    return stout


def databank_test(vc):
    boards = obtain('boards')
    chrono = obtain('chrono')
    dyadic = obtain('dyadic')
    metals = obtain('metals')
    models = obtain('models')
    resign = obtain('resign')
    silent = obtain('silent')
    stones = obtain('stones')
    toggle = obtain('toggle')

    unique = refined()

    try:
        assert len(unique) == 63, "refined 63 elementals"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    for kind in (dyadic, stones, unique):
        try:
            assert isinstance(kind, list), "instance List"
            vc.passed += 1
        except Exception as anomaly:
            vc.failed += 1
            print(vc.logist(anomaly))

    for span in len(metals), len(models):
        try:
            assert span == 13, "metals and models tridecal"
            vc.passed += 1
        except Exception as anomaly:
            vc.failed += 1
            print(vc.logist(anomaly))

    for kind in (boards, metals, models):
        try:
            assert isinstance(kind, tuple), "instance Tuple"
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


def polygraph_test(vc):
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


def laelaps_test(vc):
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


def pitchfork_test(vc):
    toggle = obtain('toggle')

    sign = 'j3'
    cord = omphalos[sign]
    pegbox = [
      sBj(cord),
      sFn(cord),
      sCn(cord),
      sGn(cord),
      sDn(cord),
      sAn(cord),
      sEn(cord),
      sBn(cord),
      sFk(cord),
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


def screenplay_test(vc):
    boards = obtain('boards')
    tuning = boards[0]

    sign = 'n0'
    cord = omphalos[sign]
    pegbox = [
      sBj(cord),
      sFn(cord),
      sCn(cord),
      sGn(cord),
      sDn(cord),
      sAn(cord),
      sEn(cord),
      sBn(cord),
      sFk(cord),
    ]

    try:
        assert layout(sign, tuning, pegbox) is None, "layout returns None"
        vc.passed += 1
    except Exception as anomaly:
        vc.failed += 1
        print(vc.logist(anomaly))

    return None


def matrices_test(vc):
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


def sentinel_test(vc):
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


def signatory_test(vc):
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

    desc = signatory_test.__name__
    print("\n\t\t{}".format(desc.upper()))
    signatory_test(vc)

    desc = sentinel_test.__name__
    print("\t\t{}\n".format(desc.upper()))
    sentinel_test(vc)

    desc = matrices_test.__name__
    print("\t\t{}\n".format(desc.upper()))
    matrices_test(vc)

    desc = screenplay_test.__name__
    print("\n\t\t{}\n".format(desc.upper()))
    screenplay_test(vc)

    desc = pitchfork_test.__name__
    print("\n\t\t{}".format(desc.upper()))
    pitchfork_test(vc)

    desc = laelaps_test.__name__
    print("\n\t\t{}".format(desc.upper()))
    laelaps_test(vc)

    desc = polygraph_test.__name__
    print("\n\t\t{}".format(desc.upper()))
    polygraph_test(vc)

    desc = databank_test.__name__
    print("\n\t\t{}".format(desc.upper()))
    databank_test(vc)

    # printout results
    vc.audition()

    return None


if __name__ == '__main__':
    scrutinize()
else:
    print("\n\t\t{}".format(__name__.upper()))
    print("Usage:\n")
    print("\twhodunit.scrutinize()\n")


