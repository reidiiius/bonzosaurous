#! /usr/bin/env python3

import re
import time

from phaedriades import omphalos


def obtain(item='toggle'):
    bank = dict(
      boards = [
        'beadgcf','bfbfb','cgdae','dadgad','dgdgbd','eadgbe','fkbjdn','unison'
      ],
      chrono = '-i' + format(time.time(), '14.3f'),
      dyadic = omphalos.items(),
      metals = [
        '__','Ti','Mn','Fe','Cu','Ag','Sn','Au','Hg','Pb','Ur','Np','Pu'
      ],
      models = [
        '_', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
      ],
      regexp = re.compile('^([ijkn]+\d+)+([lm]\d+)?h?$', re.I),
      silent = str("____ " * 12),
      stones = sorted(omphalos.keys()),
      toggle = True,
    )
    return bank[item]


def transit(cord):
    mets = obtain('metals')
    mods = obtain('models')
    if obtain('toggle'):
        wire = str(cord)
        for old, new in zip(mets, mods):
            wire = wire.replace(old, new)
        return wire
    else:
        return cord


def greyhound(bone):
    sack = list()
    for (clef, cord) in obtain('dyadic'):
        if obtain('toggle'):
            cord = transit(cord)

        if bone in cord:
            sack.append(clef)

    if len(sack) == 0:
        sack.append("{} ?".format(bone))
    return sack


def wolfhound(bone):
    sack = list()
    for clef in obtain('stones'):
        if bone in clef:
            sack.append(clef)

    if len(sack) == 0:
        sack.append("{} ?".format(bone))
    return sack


def machine(cord, gear):
    wire = transit(cord[gear:] + cord[:gear] + cord[gear:gear + 4])
    return wire


def Bj(cord):
    gear = 50
    yarn = machine(cord, gear)
    return yarn


def Fn(cord):
    gear = 25
    yarn = machine(cord, gear)
    return yarn


def Cn(cord):
    gear = 0
    yarn = machine(cord, gear)
    return yarn


def Gn(cord):
    gear = 35
    yarn = machine(cord, gear)
    return yarn


def Dn(cord):
    gear = 10
    yarn = machine(cord, gear)
    return yarn


def An(cord):
    gear = 45
    yarn = machine(cord, gear)
    return yarn


def En(cord):
    gear = 20
    yarn = machine(cord, gear)
    return yarn


def Bn(cord):
    gear = 55
    yarn = machine(cord, gear)
    return yarn


def Fk(cord):
    gear = 30
    yarn = machine(cord, gear)
    return yarn


def layout(sign, tuning, pegbox):
    print("\t" + sign + '-' + tuning + obtain('chrono'))
    for yarn in pegbox:
        print("\t" + yarn)
    return None


def beadgcf(sign, cord):
    tuning = obtain('boards')[0]
    pegbox = [
        Fn(cord),
        Cn(cord),
        Gn(cord),
        Dn(cord),
        An(cord),
        En(cord),
        Bn(cord),
    ]
    layout(sign, tuning, pegbox)
    return None


def bfbfb(sign, cord):
    tuning = obtain('boards')[1]
    saturn = Fn(cord)
    vulcan = Bn(cord)
    pegbox = [
        vulcan,
        saturn,
        vulcan,
        saturn,
        vulcan,
    ]
    layout(sign, tuning, pegbox)
    return None


def cgdae(sign, cord):
    tuning = obtain('boards')[2]
    pegbox = [
        En(cord),
        An(cord),
        Dn(cord),
        Gn(cord),
        Cn(cord),
    ]
    layout(sign, tuning, pegbox)
    return None


def dadgad(sign, cord):
    tuning = obtain('boards')[3]
    apollo = Gn(cord)
    jovian = Dn(cord)
    silver = An(cord)
    pegbox = [
        jovian,
        silver,
        apollo,
        jovian,
        silver,
        jovian,
    ]
    layout(sign, tuning, pegbox)
    return None


def dgdgbd(sign, cord):
    tuning = obtain('boards')[4]
    apollo = Gn(cord)
    jovian = Dn(cord)
    silver = An(cord)
    vulcan = Bn(cord)
    pegbox = [
        jovian,
        vulcan,
        apollo,
        jovian,
        apollo,
        jovian,
    ]
    layout(sign, tuning, pegbox)
    return None


def eadgbe(sign, cord):
    tuning = obtain('boards')[5]
    copper = En(cord)
    pegbox = [
        copper,
        Bn(cord),
        Gn(cord),
        Dn(cord),
        An(cord),
        copper,
    ]
    layout(sign, tuning, pegbox)
    return None


def fkbjdn(sign, cord):
    tuning = obtain('boards')[6]
    jovian = Dn(cord)
    aquari = Bj(cord)
    gemini = Fk(cord)
    pegbox = [
        jovian,
        aquari,
        gemini,
        jovian,
        aquari,
        gemini,
    ]
    layout(sign, tuning, pegbox)
    return None


def unison(sign, cord):
    tuning = obtain('boards')[7]
    pegbox = [
        Cn(cord),
    ]
    layout(sign, tuning, pegbox)
    return None


def govern(word):
    most = 10
    if len(word) > most:
        word = word[0:most]

    return word


def validated(sign):
    spat = obtain('regexp')
    flag = spat.match(sign) and sign in omphalos
    return flag


def fabricate(lyra, arts):
    sign = str()
    cord = str()
    for word in arts:
        sign = govern(word)
        if validated(sign):
            cord = omphalos[sign]
            print('')
            lyra(sign, cord)
        else:
            print("\n\t{} ?".format(sign))
    print('')
    return None


def pleistos(lyra=eadgbe):
    cord = str()
    print('')
    for sign in obtain('stones'):
        cord = omphalos[sign]
        print('')
        lyra(sign, cord)
        print('')
    print('')
    return None


