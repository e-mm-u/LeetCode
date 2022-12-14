def singleNumber(nums):
    # d = {}
    # for i in range(len(nums)):
    #     d[i] = 1 + d.get(nums[i],0)
    
    # for key in d :
    #     if(d[key]==1):
    #         return key
    a = 0
    for num in nums:
        a ^= num

        print(a)
    
    return a

print("ans", singleNumber([1,2,1,1,2,4]))