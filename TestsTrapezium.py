#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:57:05 2018

@author: user
"""

import unittest
from trapezium import Trapezium

class TestCalculator(unittest.TestCase):
    _tmp = Trapezium()
    def testBaseLarge(self):
        self.assertEqual(int(self._tmp.getTrapeziumBaseLarge()), 741)
    
    def testBaseSmall(self):
        self.assertEqual(int(self._tmp.getTrapeziumBaseSmall()), 403)
    
    def testHeight(self):
        self.assertEqual(int(self._tmp.getTrapeziumHeight()), 466)
    
    def testZeroPointPosition(self):
        _tmp1 = self._tmp.getZeroPointPosition()
        _tmp1 = [int(_tmp1[0]),int(_tmp1[1])]
        self.assertEqual(_tmp1, [200,-39])

if __name__ == "__main__":
    unittest.main()
    