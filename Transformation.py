'''
Convert camera coordinates to plane coordinates
'''
import Sources

def Transformation(SourceCoordinatesPx,
                   TrapeziumBaseLarge,
                   TrapeziumBaseSmall,
                   TrapeziumHeight,
                   ZeroPointPosition):
#    ZeroXBaseLargeMm = TrapeziumBaseLarge/2
#    ZeroXBaseSmallMm = TrapeziumBaseSmall/2
#    ZeroXCoordinatesPx = Sources.VideoResolutionScaled[0]/2
    ZeroXCoordinatesPx = Sources.VideoResolution[0]/2

    XToZeroPx = SourceCoordinatesPx[0] - ZeroXCoordinatesPx

#    XToZeroLargeMm = XToZeroPx * TrapeziumBaseLarge / Sources.VideoResolutionScaled[0]
#    XToZeroSmallMm = XToZeroPx * TrapeziumBaseSmall / Sources.VideoResolutionScaled[0]
    XToZeroLargeMm = XToZeroPx * TrapeziumBaseLarge / Sources.VideoResolution[0]
    XToZeroSmallMm = XToZeroPx * TrapeziumBaseSmall / Sources.VideoResolution[0]

#    DeltaXMm_Px = (XToZeroLargeMm - XToZeroSmallMm) / Sources.VideoResolutionScaled[1]
    DeltaXMm_Px = (XToZeroLargeMm - XToZeroSmallMm) / Sources.VideoResolution[1]

    XToZeroMm = XToZeroSmallMm + SourceCoordinatesPx[1] * DeltaXMm_Px

#    YToZeroMm = SourceCoordinatesPx[1] * TrapeziumHeight / Sources.VideoResolutionScaled[1]
    YToZeroMm = SourceCoordinatesPx[1] * TrapeziumHeight / Sources.VideoResolution[1]

    SiteCoordinates = [0,0]
    SiteCoordinates[0] = XToZeroMm + ZeroPointPosition[0]
    SiteCoordinates[1] = YToZeroMm + ZeroPointPosition[1]
    return SiteCoordinates