

def getBondPrice_E(face, couponRate, yc):
    
    pvcf = 0
    
    for i in range(5):
        if yc[i] == yc[-1]:
            c = face * couponRate + face
            pv = (1 + yc[i]) ** (-i - 1)
            pvcf = pvcf + c * pv
            
        else:
            c = face * couponRate
            pv = (1 + yc[i]) ** (-i - 1)
            pvcf = pvcf + c * pv
    
    return(pvcf)

