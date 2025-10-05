

def getBondDuration(y, face, couponRate, m, ppy = 1):
    
    wsum = 0
    wtsum = 0
    periodicYield = y / ppy
    msum = m * ppy
        
    for i in range(1,msum+1):
        if i == msum:
            wsum = wsum + (1 + periodicYield) ** (-i) * (face * couponRate / ppy + face)
            wtsum = wtsum + (1 + periodicYield) ** (-i) * (face * couponRate / ppy + face) * (i / ppy)
        else:
            wsum = wsum + (1 + periodicYield) ** (-i) * face * couponRate / ppy
            wtsum = wtsum + (1 + periodicYield) ** (-i) * face * couponRate / ppy * (i / ppy)
        
    x = wtsum / wsum
    return(x)
