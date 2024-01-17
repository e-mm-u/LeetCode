class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = [False]*len(arr)
        unique_values = set(arr)
        for item in unique_values:
            t = arr.count(item)
            if(d[t-1])==True:
                return False
            d[t-1]=True
        return True