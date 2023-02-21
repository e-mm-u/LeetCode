
def getRow(rowIndex):
    if rowIndex==0:
        return [1]
    elif rowIndex==1:
        return [1,1] 

    tri = [1,1]
    for i in range(2,rowIndex+1):
        res = []
        res.append(1)
        for j in range(len(tri)-1):
            res.append(tri[j]+tri[j+1])
        res.append(1)

        tri = [i for i in res]

    return tri