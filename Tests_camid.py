#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:57:05 2018

@author: user
"""

import unittest
from camid import CamId

class TestCalculator(unittest.TestCase):
    def test_isCurrentInit(self):
        _tmp = CamId()
        self.assertEqual(_tmp.isCurrent([5,7]), False)
    
    def test_isCurrentBigger(self):
        _tmp = CamId()
        _tmp.isCurrent([50,150])
        self.assertEqual(_tmp.isCurrent([5,7]), False)
    
    def test_isCurrentNormal(self):
        _tmp = CamId()
        _tmp.isCurrent([20,20])
        self.assertEqual(_tmp.isCurrent([5,7]), True)

if __name__ == "__main__":
    unittest.main()
