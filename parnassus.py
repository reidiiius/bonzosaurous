#! /usr/bin/env python3

"""Module parnassus provides data and routines to model tonal inversions."""

import re
import time

from phaedriades import omphalos


def refined():
    """List of tonal inversion strings."""
    unique = list()
    vessel = list()
    for clef, cord in omphalos.items():
        vessel.extend(cord.split())

    assets = set(vessel); chex5f = chr(95)
    if obtain('toggle'):
        unique = [
          transit(word) for word in assets if chex5f not in word
        ]
    else:
        unique = [ word for word in assets if chex5f not in word ]

    return sorted(unique)


def horolog():
    epoch = format(time.time(), '14.3f')
    return epoch


def obtain(item='toggle'):
    """Dictionary of useful things."""
    bank = dict(
      boards = (
        'beadgcf','bfbfb','cgdae','dadgad','dgdgbd','eadgbe','fkbjdn','unison'
      ),
      chrono = "-i{}".format(horolog()),
      dyadic = list(omphalos.items()),
      metals = (
        '__','Ti','Mn','Fe','Cu','Ag','Sn','Au','Hg','Pb','Ur','Np','Pu'
      ),
      models = (
        '_', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
      ),
      resign = '^([ijkn]+\d+)+([lm]\d+)?h?$',
      silent = str("____ " * 12),
      stones = sorted(omphalos.keys()),
      toggle = True,
    )
    return bank[item]


def choices():
    """String of instrument tunings."""
    zithers = obtain('boards')
    attuned = chr(32).join(zithers)
    print("\t{}\n".format(attuned))

    return None


def chalkboard(clefs):
    """Tabulates given list."""
    accum = str()
    count = int()
    for sign in clefs:
        accum = accum + "\t{}".format(sign)
        count = count + 1
        if count % 7 == 0:
            accum = accum + "\n"

    print("\n{}".format(accum))
    if count % 7 != 0:
        print('')
    return None


def transit(cord):
    """Transcribes given string."""
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
    """List of keys related by given tonality."""
    sack = list()
    for (clef, cord) in obtain('dyadic'):
        if obtain('toggle'):
            cord = transit(cord)

        if bone in cord:
            sack.append(clef)

    if len(sack) == 0:
        sack.append("{} ?".format(bone))
    return sorted(sack)


def wolfhound(bone):
    """List of keys related by given signature."""
    sack = list()
    for clef in obtain('stones'):
        if bone in clef:
            sack.append(clef)

    if len(sack) == 0:
        sack.append("{} ?".format(bone))
    return sack


def machine(cord, gear):
    """Slices given string using given integer index."""
    wire = transit(cord[gear:] + cord[:gear] + cord[gear:gear + 4])
    return wire


def sBj(cord):
    """Permute given string to B flat."""
    gear = 50
    yarn = machine(cord, gear)
    return yarn


def sFn(cord):
    """Permute given string to F natural."""
    gear = 25
    yarn = machine(cord, gear)
    return yarn


def sCn(cord):
    """Given string stays relative C natural."""
    gear = 0
    yarn = machine(cord, gear)
    return yarn


def sGn(cord):
    """Permute given string to G natural."""
    gear = 35
    yarn = machine(cord, gear)
    return yarn


def sDn(cord):
    """Permute given string to D natural."""
    gear = 10
    yarn = machine(cord, gear)
    return yarn


def sAn(cord):
    """Permute given string to A natural."""
    gear = 45
    yarn = machine(cord, gear)
    return yarn


def sEn(cord):
    """Permute given string to E natural."""
    gear = 20
    yarn = machine(cord, gear)
    return yarn


def sBn(cord):
    """Permute given string to B natural."""
    gear = 55
    yarn = machine(cord, gear)
    return yarn


def sFk(cord):
    """Permute given string to F sharp."""
    gear = 30
    yarn = machine(cord, gear)
    return yarn


def layout(sign, tuning, pegbox):
    """Printout headline and subsequent strings."""
    print("\t" + sign + '-' + tuning + obtain('chrono'))
    for yarn in pegbox:
        print("\t" + yarn)
    return None


def beadgcf(sign, cord):
    """Perfect fourths tuning."""
    tuning = obtain('boards')[0]
    pegbox = [
        sFn(cord),
        sCn(cord),
        sGn(cord),
        sDn(cord),
        sAn(cord),
        sEn(cord),
        sBn(cord),
    ]
    layout(sign, tuning, pegbox)
    return None


def bfbfb(sign, cord):
    """Tritones tuning."""
    tuning = obtain('boards')[1]
    saturn = sFn(cord)
    vulcan = sBn(cord)
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
    """Perfect fifths tuning."""
    tuning = obtain('boards')[2]
    pegbox = [
        sEn(cord),
        sAn(cord),
        sDn(cord),
        sGn(cord),
        sCn(cord),
    ]
    layout(sign, tuning, pegbox)
    return None


def dadgad(sign, cord):
    """Celtic tuning."""
    tuning = obtain('boards')[3]
    apollo = sGn(cord)
    jovian = sDn(cord)
    silver = sAn(cord)
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
    """Open G tuning."""
    tuning = obtain('boards')[4]
    apollo = sGn(cord)
    jovian = sDn(cord)
    silver = sAn(cord)
    vulcan = sBn(cord)
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
    """Guitar Standard tuning."""
    tuning = obtain('boards')[5]
    copper = sEn(cord)
    pegbox = [
        copper,
        sBn(cord),
        sGn(cord),
        sDn(cord),
        sAn(cord),
        copper,
    ]
    layout(sign, tuning, pegbox)
    return None


def fkbjdn(sign, cord):
    """Major thirds tuning."""
    tuning = obtain('boards')[6]
    jovian = sDn(cord)
    aquari = sBj(cord)
    gemini = sFk(cord)
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
    """Unison tuning."""
    tuning = obtain('boards')[7]
    pegbox = [
        sCn(cord),
    ]
    layout(sign, tuning, pegbox)
    return None


def govern(word):
    """Limit amount of characters in given word."""
    most = 10
    if len(word) > most:
        word = word[0:most]
    return word


def validated(sign):
    """Compare given word against rational pattern."""
    spat = obtain('resign')
    flag = re.match(spat, sign) and sign in omphalos
    return flag


def fabricate(lyra, arts):
    """Printout given key list with given tuning function."""
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
    """Printout all keys with given tuning function."""
    cord = str()
    print('')
    for sign in obtain('stones'):
        cord = omphalos[sign]
        print('')
        lyra(sign, cord)
        print('')
    print('')
    return None


