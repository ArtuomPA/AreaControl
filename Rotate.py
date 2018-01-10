import Sources

def Rotate(crdnt):
    Hx = Sources.CamCentersDelta[0]
    Hy = Sources.CamCentersDelta[1]
    
    return [Hx-crdnt[0], Hy-crdnt[1]]