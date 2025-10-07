

def getBondPrice_E(face, couponRate, yc):
    
    pvcf = 0
    
    for i,j in enumerate(yc):
        if j == yc[-1]:
            c = face * couponRate + face
            pv = (1 + j) ** (-i - 1)
            pvcf = pvcf + c * pv
            
        else:
            c = face * couponRate
            pv = (1 + j) ** (-i - 1)
            pvcf = pvcf + c * pv
    
    return(pvcf)
