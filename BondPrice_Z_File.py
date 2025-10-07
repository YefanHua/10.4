

def getBondPrice_Z(face, couponRate, times, yc):
        
    pvcf = 0
    
    for i,j in zip(yc,times):
        if i == yc[-1]:
            c = face * couponRate + face
            pv = (1 + i) ** (-j)
            pvcf = pvcf + c * pv
            
        else:
            c = face * couponRate
            pv = (1 + i) ** (-j)
            pvcf = pvcf + c * pv
    
    return(pvcf)
