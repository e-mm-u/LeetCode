class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        
        total = n-1
        last = total*4
        
        ans = (4+last)*total//2
        return ans+1
        