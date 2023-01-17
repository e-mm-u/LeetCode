class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for i in range(len(s)):
            if s[i] in d :
                d[s[i]] = True
            else :
                d[s[i]] = False
            
        for i in range(len(s)):
            if d[s[i]] == False:
                return i
            
        return -1