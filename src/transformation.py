#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sources


def Transformation(SourceCoordinatesPx,
                   TrapeziumBaseLarge,
                   TrapeziumBaseSmall,
                   TrapeziumHeight,
                   ZeroPointPosition):
    ZeroXCoordinatesPx = sources.VideoResolution[0]/2

    XToZeroPx = SourceCoordinatesPx[0] - ZeroXCoordinatesPx

    XToZeroLargeMm = XToZeroPx * TrapeziumBaseLarge / sources.VideoResolution[0]
    XToZeroSmallMm = XToZeroPx * TrapeziumBaseSmall / sources.VideoResolution[0]

    DeltaXMm_Px = (XToZeroLargeMm - XToZeroSmallMm) / sources.VideoResolution[1]

    XToZeroMm = XToZeroSmallMm + SourceCoordinatesPx[1] * DeltaXMm_Px

    YToZeroMm = SourceCoordinatesPx[1] * TrapeziumHeight / sources.VideoResolution[1]

    SiteCoordinates = [0,0]
    SiteCoordinates[0] = XToZeroMm + ZeroPointPosition[0]
    SiteCoordinates[1] = YToZeroMm + ZeroPointPosition[1]

    return SiteCoordinates
