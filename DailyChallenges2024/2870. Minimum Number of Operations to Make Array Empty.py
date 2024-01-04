class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def times(x):
            if x%3==0:
                return x//3
            else:
                return x//3+1

        nums.sort()
        t = nums[0]
        cnt,res = 0,0    
        for i in range(len(nums)):
            if nums[i]==t:
                cnt += 1
            else:
                if cnt==1:
                    return -1
                res += times(cnt)
                t = nums[i]
                cnt = 1
        if cnt==1:
            return -1
        
        res += times(cnt)

        return res

                
