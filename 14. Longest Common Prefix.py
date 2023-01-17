class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        l = len(strs[0])
        small = strs[0]
        for i in range(0,len(strs)):
            if len(strs[i])<l:
                l = len(strs[i])
                small = strs[i]
                
            
        res = ""
        i = 0
        while i<l:
            
            for s in strs:
                if s[i]!=strs[0][i]:
                    return res
                
            res += strs[0][i]
            i += 1
            
                    
                
        return res

                
                
            
            
        