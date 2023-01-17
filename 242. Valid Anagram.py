class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s) :
            return False
        
        d = {}
        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) +1
            
        for i in range(len(t)):
            if t[i] in d:
                d[t[i]] -= 1
                if d[t[i]] < 0:
                    return False
            else :
                return False
        return True