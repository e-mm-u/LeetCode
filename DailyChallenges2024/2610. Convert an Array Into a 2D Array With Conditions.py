class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while True:
            if len(set(nums))==1 and False in set(nums):
                break

            t = []
            for j in range(len(nums)):
                if nums[j] and nums[j] not in t:
                    t.append(nums[j])
                    nums[j] = False
            res.append(t)
        
        return res
                
