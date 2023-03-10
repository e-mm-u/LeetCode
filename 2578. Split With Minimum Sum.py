class Solution:
    def splitNum(self, num: int) -> int:
        nums = []
        while num:
            r = num%10
            nums.append(r)
            num = num//10
        nums.sort()
        
        num1 = 0
        num2 = 0
        
        for i in range(0,len(nums),2):
            num1 = num1*10+nums[i]
        for i in range(1,len(nums),2):
            num2 = num2*10 + nums[i]
        
        return num1+num2