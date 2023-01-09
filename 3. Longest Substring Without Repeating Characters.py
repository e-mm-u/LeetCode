def lengthOfLongestSubstring(s):
    res = 0
    i = 0
    while i<len(s):
        j = i
        sub = ''
        while(j<len(s)):
            if s[j] not in sub:
                sub += s[j]
                res = max(res,len(sub))
                j += 1
            else : 
                break
        i += 1

    print(res)
    return res

s = "abcabcbb"
s = " "
s = "avaf"
lengthOfLongestSubstring(s)