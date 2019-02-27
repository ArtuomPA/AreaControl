#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rotate import Rotate


def Compare(crdnt1, crdnt2):
    x1 = crdnt1[0]
    y1 = crdnt1[1]

    x2_1, y2_1 = Rotate(crdnt2)
    return [x1-x2_1, y1-y2_1]
