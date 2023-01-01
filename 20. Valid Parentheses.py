
def isValid(s):
    h = {")" : "(" , "}" : "{", "]" : "[" }
    arr = []

    for i in s :
        if i in h:
            if arr and arr[-1] == h[i]:
                arr.pop()
            else :
                return False
        else :
            arr.append(i)
    
    if(arr):
        return False
    else :
        return True