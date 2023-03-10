class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        d = {}
        for i in range(1,max(arr)+1):
            d[i] = True
        
        
        for i in arr:
            if d[i]:
                d[i] = False
        
        c = 0
        for key in d:
            if d[key]:
                c += 1
                if c==k:
                    return key
        
        return arr[-1]+k-c