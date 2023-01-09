# using for loop
def findMin(nums):
    for i in range(len(nums)):
        if(nums[i]<=nums[-1]):
            return nums[i]

# using binary search
def findMin(nums):
    lo,hi = 0,len(nums)-1
    res = nums[0]
    while(lo<hi):
        if(nums[lo]>nums[hi]):
            mid = (lo+hi)//2

            if nums[mid]>=nums[lo]:
                lo = mid+1
                res = nums[lo]
            else:
                hi = mid
                res = nums[mid]
            
        else:
            res = nums[lo]
            break
        
    return res
    

nums = [3,4,5,1]
nums= [5,6,7,8,9,0,1,2,3,4,5,5,5,5]
nums = [3,4,5,1,2]
nums  = [4,5,6,7,0,1,2]
# nums = [2,1]
# nums=[1]
print(findMin(nums))