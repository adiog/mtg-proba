# -*- coding: utf-8 -*-

"""
This file is a part of mtg-proba project.
Copyright (c) 2017 Aleksander Gajewski <adiog@brainfuck.pl>.
"""

from unittest import TestCase

from bigfloat import quadruple_precision

from proba import fac, bin, partial_sum, sequence, exactly, with_range, compute


class ProbaTestCase(TestCase):
    def assertBigFloat(self, f1, f2):
        self.assertAlmostEqual(float(f1), float(f2), places=4)

    def test_fac(self):
        self.assertEqual(fac(0), 1)
        self.assertEqual(fac(1), 1)
        self.assertEqual(fac(5), 120)

    def test_bin(self):
        self.assertEqual(bin(5,-1), 0)
        self.assertEqual(bin(5,0), 1)
        self.assertEqual(bin(5,1), 5)
        self.assertEqual(bin(5,2), 10)
        self.assertEqual(bin(5,3), 10)
        self.assertEqual(bin(5,4), 5)
        self.assertEqual(bin(5,5), 1)
        self.assertEqual(bin(5,6), 0)

    def test_partial_sum(self):
        self.assertEqual(partial_sum([]), [0])
        self.assertEqual(partial_sum([1,2,3]), [0,1,3])

    def test_sequence(self):
        self.assertEqual(sequence(4, [2,1]), 24)
        self.assertEqual(sequence(6, [2,1,1]), 360)

    def test_exactly(self):
        with quadruple_precision:
            self.assertAlmostEqual(float(exactly(7, 60, [(0,4)])), 0.6005, places=4)

    def test_with_range(self):
        self.assertAlmostEqual(float(with_range(10, 60, 10, [], [(4,10,20)])), 0.4405, places=4)

    def test_compute(self):
        self.assertBigFloat(compute(7, 60, '0-4/4'), 1)
        self.assertBigFloat(compute(7, 40, '0/17'), 0.0131)
        self.assertBigFloat(compute(7, 40, '1/17'), 0.0920)
        self.assertBigFloat(compute(7, 40, '2-3/17'), 0.5684)
        self.assertBigFloat(compute(7, 40, '4/17'), 0.2261)
        self.assertBigFloat(compute(7, 40, '5/17'), 0.0840)
        self.assertBigFloat(compute(7, 40, '6+/17'), 0.0163)
        self.assertBigFloat(compute(7, 40, '7/17'), 0.0010)
        self.assertBigFloat(compute(7, 60, '2-3/23 1+/4 1+/3'), 0.0694)
        self.assertBigFloat(compute(7, 60, '2+/23 1+/4 1+/4 1+/4'), 0.0278)
        self.assertBigFloat(compute(7, 60, '1+/17 1+/4 1+/4 1+/4 1+/6'), 0.0134)
