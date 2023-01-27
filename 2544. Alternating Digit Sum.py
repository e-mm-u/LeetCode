def alternateDigitSum(n):
    sign = 1
    s = str(n)
    res = 0
    for i in range(len(s)):
        n = s[i]
        res += sign* (ord(n)-ord('0'))
        sign *= -1
    return res
        