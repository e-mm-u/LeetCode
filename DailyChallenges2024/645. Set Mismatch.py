class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mapp = [False]*n
        xtra, missing = 0, 0

        for num in nums:
            if mapp[num-1]:
                xtra = num
            mapp[num-1] = True
        # print(mapp)
        for i in range(n):
            if not mapp[i]:
                missing = i+1
   
        return [xtra, missing]