def xorBeauty(nums):
    res = 0
    for i in range(len(nums)):
        res = res ^ nums[i]
    return res