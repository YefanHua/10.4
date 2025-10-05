

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    pvsum= 0
    msum = m * ppy
    
    for i in range(1,msum+1):
        pvsum = pvsum + (1 + y / ppy) ** (-i)
    
    pvlast = (1 + y / ppy) ** (-msum)
    
    x = (pvsum * couponRate / ppy + pvlast) * face
    
    return(x)
