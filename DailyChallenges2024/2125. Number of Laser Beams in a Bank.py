class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        def ones(s):
            c = 0
            for char in s:
                if char=='1':
                    c+=1
            return c
        
        t_arr = []
        for s in bank:
            t = ones(s)
            if t>0:
                t_arr.append(t)
        if len(t_arr)==1:
            return 0

        i,j = 0,1
        res = 0
        while j<len(t_arr):
            res += t_arr[i]*t_arr[j]
            i += 1
            j += 1
        
        return res


