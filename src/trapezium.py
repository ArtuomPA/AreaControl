#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def toRad(x):
    return x * 0.0175


class Trapezium:
    def __init__(self,
                 VideoResolut = [1921, 1081],
                 TopLensAngle = 49.1,
                 CamPosition = [0, 700, 355],
                 CamTilting = 50,
                 PlainDimensions = [400, 800]):
        self.__TopLensAngle = toRad(TopLensAngle)
        self.__CamPosition = CamPosition
        self.__CamTilting = toRad(CamTilting)
        self.__PlainDimensions = PlainDimensions

        self.__TrapeziumBaseLarge = None
        self.__TrapeziumBaseSmall = None
        self.__TrapeziumHeight = None
        self.__ZeroPointPosition = None

        self.__SideLensAngle = self.__TopLensAngle * VideoResolut[1] /\
            VideoResolut[0]
        self.__calc()

    #calc 2
    def __SmallAngle(self):
        return self.__CamTilting - self.__SideLensAngle/2

    def __BigAngle(self):
        return self.__CamTilting + self.__SideLensAngle/2

    #calc 3
    def __a(self, CamPosition, SmallAngle):
        return (CamPosition[2]) * math.tan(SmallAngle)

    def __b(self, CamPosition, BigAngle):
        return (CamPosition[2]) * math.tan(BigAngle)

    #calc 4
    def __Ca(self, CamPosition, a):
        return math.sqrt(CamPosition[2] * CamPosition[2] + a * a)

    def __Da(self, TopLensAngle, Ca):
        return 2 * math.tan(TopLensAngle/2) * Ca

    #calc 5
    def __Cb(self, CamPosition, b):
        return math.sqrt(CamPosition[2] * CamPosition[2] + b * b)

    def __Db(self, TopLensAngle, Cb):
        return 2 * math.tan(TopLensAngle/2) * Cb

    #calc 6
    def __ZeroPoint(self, PlainDimensions, CamPosition, a):
        return [
                PlainDimensions[0] / 2,
                a - (CamPosition[1] - PlainDimensions[1] / 2)
                ]

    def __calc(self):
        self.__TrapeziumBaseLarge = self.__Db(
            self.__TopLensAngle,
            self.__Cb(
                self.__CamPosition,
                self.__b(
                    self.__CamPosition, self.__BigAngle()
                    )
                )
            )

        self.__TrapeziumBaseSmall = self.__Da(
            self.__TopLensAngle,
            self.__Ca(
                self.__CamPosition,
                self.__a(
                    self.__CamPosition, self.__SmallAngle()
                    )
                )
            )

        self.__TrapeziumHeight = (
            self.__b(self.__CamPosition, self.__BigAngle()) - 
            self.__a(self.__CamPosition, self.__SmallAngle())
            )

        self.__ZeroPointPosition = self.__ZeroPoint(
            self.__PlainDimensions,
            self.__CamPosition,
            self.__a(self.__CamPosition, self.__SmallAngle())
            )

    def getTrapeziumBaseLarge(self):
        return self.__TrapeziumBaseLarge

    def getTrapeziumBaseSmall(self):
        return self.__TrapeziumBaseSmall

    def getTrapeziumHeight(self):
        return self.__TrapeziumHeight

    def getZeroPointPosition(self):
        return self.__ZeroPointPosition
