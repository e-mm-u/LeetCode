def generate(n):
    tri = [[1],[1,1]]
    if n==1:
        return [tri[0]]
    elif n==2:
        return tri
    else:
        for i in range(2,n):
            prev = tri[-1]
            res = [1]
            for j in range(len(prev)-1): #cause we the middle values here only, not the first and last one
                res.append(prev[j]+prev[j+1])
            res.append(1)
            tri.append(res)
    return tri
def generate_(n):
    tri = [[1]]
    
    for i in range(n-1):
        temp = [0]+tri[-1]+[0]
        res = []
        for j in range(len(temp)-1):
            res.append(temp[j]+temp[j+1])
        
        tri.append(res)
    return tri

z = generate(5)
z = generate(1)
z = generate(2)
z = generate(3)
z = generate(4)

z = generate_(5)
# z = generate_(1)
# z = generate_(2)
# z = generate_(3)
# z = generate_(4)

for k in z:
    print(k)

