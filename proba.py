# -*- coding: utf-8 -*-

"""
This file is a part of mtg-proba project.
Copyright (c) 2017 Aleksander Gajewski <adiog@brainfuck.pl>.
"""

import itertools
from bigfloat import BigFloat


def fac(n):
    if n == 0 or n == 1:
        return BigFloat(1)
    else:
        r = BigFloat(1)
        for i in range(n):
            r = r * BigFloat(i+1)
        return r


def bin(n,k):
    if k < 0 or k > n:
        return BigFloat(0)
    else:
        return fac(n) / fac(k) / fac(n-k)


def bin_of_seq(cards):
    result = BigFloat(1)
    for p,P in cards:
        result = result * bin(P, p)
    return result


def partial_sum(l):
    return [s for s in itertools.accumulate([0] + l[:-1])]


def sequence(set_size, cards):
    if sum(cards) > set_size:
        return 0
    adjust = partial_sum(cards)
    result = BigFloat(1)
    for i,c in enumerate(cards):
        result = result * bin(set_size-adjust[i], c) * fac(c)
    return result


def exactly(hand, deck, cards):
    card_in = [p for (p,P) in cards]
    card_all = [P for (p,P) in cards]
    card_out = [P-p for (p,P) in cards]

    return bin_of_seq(cards) * sequence(hand, card_in) * sequence(deck-hand, card_out) * fac(deck - sum(card_all)) / fac(deck)


def with_range(hand, deck, slots, cards, ranges):
    if not ranges:
        ret = exactly(hand, deck, cards)
        print(hand, deck, cards, ret)
        return ret
    else:
        result = BigFloat(0)
        (card_in_min, card_in_max, card_all) = ranges[0]
        for card_in in range(card_in_min, card_in_max+1):
            if slots-card_in >= 0:
                result = result + with_range(hand, deck, slots-card_in, cards + [(card_in, card_all)], ranges[1:])
        return result


def parse_as_min_max_all(s, limit):
    min_max, sall = s.split('/')
    iall = int(sall)
    if '+' in min_max:
        imax = min(iall, limit)
        return (int(min_max[:-1]), imax, iall)
    elif min_max[0] == '-':
        return (0, int(min_max[1:]), iall)
    elif '-' in min_max:
        smin, smax = min_max.split('-')
        return (int(smin), int(smax), iall)
    else:
        mm = int(min_max)
        return (mm, mm, iall)


def compute(hand, deck, input_string):
    return with_range(hand, deck, hand, [], [parse_as_min_max_all(input_part, hand) for input_part in input_string.split(' ')])
