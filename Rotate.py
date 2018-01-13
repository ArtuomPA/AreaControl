import Sources

def Rotate(crdnt):
    Hx = Sources.PlainDimensions[0]
    Hy = Sources.PlainDimensions[1]
    
    return [Hx-crdnt[0], Hy-crdnt[1]]