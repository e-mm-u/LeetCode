class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds = {}
        for char in s:
            ds[char] = ds.get(char, 0)+1
        
        dt = {}
        for char in t:
            dt[char] = dt.get(char, 0)+1
        
        keys = ds.keys()
        steps = 0
        for k in keys:
            if k in dt:
                if ds[k]>dt[k]:
                    steps += ds[k]-dt[k]
            else:
                steps += ds[k]

        return steps
