def threeSum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums)-2):
        p1,p2 = i+1, len(nums)-1
        while(p1<p2):
            curr_sum = nums[i] + nums[p1] + nums[p2]

            if(curr_sum==0):
                if [nums[i],nums[p1],nums[p2]] not in ans:
                    ans.append([nums[i],nums[p1],nums[p2]])
                p1 += 1
            elif(curr_sum>0):
                p2 -= 1
            else :
                p1 += 1
    return ans