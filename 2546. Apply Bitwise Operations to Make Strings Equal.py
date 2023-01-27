s = "11"
t = "00"
# latest 
def makeStringsEqual(s, target):
    
    if s==target:
        return True
    if '1' not in s or '1' not in target:
        return False
    return True

# 2nd latest
def makeStringsEqual(s, target):
    
    if s==target:
        return True
    
    length = len(s)-1
    sum_s = 0
    sum_t = 0
    
    while length>=0 :
        sum_s += int(s[length])
        sum_t += int(target[length])
        length -= 1
    
    if sum_t==0 or sum_s==0:
        return False

    return True

# first
def fnc(s,t):
    if s==t:
        return True
    st = [ int(s[i]) for i in range(len(s)) ]
    tr = [ int(t[i]) for i in range(len(t)) ]

    if sum(tr)==0 or sum(st)==0:
        return False

    return True

res = fnc(s,t)
print(res)
