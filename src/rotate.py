#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sources


def Rotate(crdnt):
    Hx = sources.PlainDimensions[0]
    Hy = sources.PlainDimensions[1]

    return [Hx-crdnt[0], Hy-crdnt[1]]
