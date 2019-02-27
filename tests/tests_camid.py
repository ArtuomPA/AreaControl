#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from src.camid import CamId


class TestCalculator(unittest.TestCase):
    def test_isCurrentInit(self):
        _tmp = CamId()

        res = _tmp.isCurrent([5,7])

        self.assertEqual(False, res)

    def test_isCurrentBigger(self):
        _tmp = CamId()
        _tmp.isCurrent([50,150])

        res = _tmp.isCurrent([5,7])

        self.assertEqual(False, res)

    def test_isCurrentNormal(self):
        _tmp = CamId()
        _tmp.isCurrent([20,20])

        res = _tmp.isCurrent([5,7])

        self.assertEqual(True, res)

if __name__ == "__main__":
    unittest.main()
