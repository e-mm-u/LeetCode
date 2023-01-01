#  @e-mm-u

#  brute force solution || time complexity O(n^2) || space complexity O(1)
class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums), 1):
                if(nums[i]+nums[j]==target):
                    return [i,j]
# O(n^2) O(1)
class Solution:
    def twoSum(nums, target):
        while (len(nums)):
            
            y = len(nums)-1
            t = target - nums[y]
            nums.pop()
            
            for i in range(len(nums)):
                if nums[i]==t:
                    return [i,y]
                