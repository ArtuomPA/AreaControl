'''
Convert camera coordinates to plane coordinates
'''
import Sources

def Transformation(SourceCoordinatesPx):
#    ZeroXBaseLargeMm = Sources.LensBaseLarge/2
#    ZeroXBaseSmallMm = Sources.LensBaseSmall/2
#    ZeroXCoordinatesPx = Sources.LensResolutionScaled[0]/2
    ZeroXCoordinatesPx = Sources.LensResolution[0]/2

    XToZeroPx = SourceCoordinatesPx[0] - ZeroXCoordinatesPx

#    XToZeroLargeMm = XToZeroPx * Sources.LensBaseLarge / Sources.LensResolutionScaled[0]
#    XToZeroSmallMm = XToZeroPx * Sources.LensBaseSmall / Sources.LensResolutionScaled[0]
    XToZeroLargeMm = XToZeroPx * Sources.LensBaseLarge / Sources.LensResolution[0]
    XToZeroSmallMm = XToZeroPx * Sources.LensBaseSmall / Sources.LensResolution[0]

#    DeltaXMm_Px = (XToZeroLargeMm - XToZeroSmallMm) / Sources.LensResolutionScaled[1]
    DeltaXMm_Px = (XToZeroLargeMm - XToZeroSmallMm) / Sources.LensResolution[1]

    XToZeroMm = XToZeroSmallMm + SourceCoordinatesPx[1] * DeltaXMm_Px

#    YToZeroMm = SourceCoordinatesPx[1] * Sources.LensHeight / Sources.LensResolutionScaled[1]
    YToZeroMm = SourceCoordinatesPx[1] * Sources.LensHeight / Sources.LensResolution[1]

    SiteCoordinates = [0,0]
    SiteCoordinates[0] = XToZeroMm + Sources.ZeroPointPosition[0]
    SiteCoordinates[1] = YToZeroMm + Sources.ZeroPointPosition[1]
    return SiteCoordinates