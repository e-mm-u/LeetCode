class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        l = len(nums)
        
        for i in range(0,l,1):
            
            x = nums[nums[i]]
            ans.append(x)
            
        return ans
