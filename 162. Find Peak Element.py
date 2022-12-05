def findPeakElement(nums):
    
    return binarySearch(nums)

def binarySearch(nums):
    start, end = 0, len(nums)-1
    while(start<end):
        # print("start : ", start, "end :", end)
        mid = int((start+end)/2)
        # print('mid', mid)

        # if nums[mid] < nums[mid+1] -> increasing order
        if(nums[mid]<nums[mid+1]):
            # print('increasing part')
            start = mid + 1
            # print('start ', start)

        # if nums[mid] > nums[mid+1] -> decreasing order
        else:
            # print('decreasing part')
            end = mid
            # print('end ', end)

    return start


nums = [1,2,1,3,5,6,4]
findPeakElement(nums)

