#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from src.trapezium import Trapezium


class TestCalculator(unittest.TestCase):
    def __init__(self):
        self.calc = Trapezium()

    def testBaseLarge(self):
        res = int(self.calc.getTrapeziumBaseLarge())

        self.assertEqual(741, res)

    def testBaseSmall(self):
        res = int(self.calc.getTrapeziumBaseSmall())

        self.assertEqual(403, res)

    def testHeight(self):
        res = int(self.calc.getTrapeziumHeight())

        self.assertEqual(466, res)

    def testZeroPointPosition(self):
        res = self.calc.getZeroPointPosition()
        res = [int(res[0]),int(res[1])]
        self.assertEqual([200,-39], res)


if __name__ == "__main__":
    unittest.main()
