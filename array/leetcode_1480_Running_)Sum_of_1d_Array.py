class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        ans.append(nums[0])
        l = len(nums)
        
        for i in range(1,l,1):
            ans.append(ans[i-1]+nums[i])
            
        return ans