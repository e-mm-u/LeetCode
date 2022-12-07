def removeDuplicates(nums):
    
    pointer_index = 1

    for i in range(1,len(nums),1):
        if(nums[i] == nums[i-1]):
            continue
        else:
            nums[pointer_index] = nums[i]
            pointer_index += 1

    return pointer_index

nums = [1,1,2,2,2,3,4,5,5,6]
res = removeDuplicates(nums)
print(res, nums)