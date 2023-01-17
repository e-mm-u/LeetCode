class Solution:
    def myAtoi(self, s: str) -> int:
        Min,Max = -2147483648,2147483647
        ans,sign,j = 0,1,0

        for i in range(len(s)):
            if s[i] == " ":
                continue
            elif s[i]=='+':
                j = i+1
                break
            elif s[i]=='-':
                sign = -1
                j = i+1
                break
            elif 0<=ord(s[i])-ord('0')<=9:
                j = i
                break
            else:
                return ans
        
        while j<len(s):
            
            n = ord(s[j])-ord('0')
            
            if 0<=n<=9:
                ans = ans*10 + n
            else:
                break
                
            j += 1
        
        if sign*ans<Min:
            return Min
        elif sign*ans>Max:
            return Max
        
        return ans*sign