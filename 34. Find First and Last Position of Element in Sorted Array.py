def searchRange(nums,target):
    ans = [-1,-1]

    ans[0] = binarySearch(nums,target, True)
    if(ans[0] != -1):
        print('lets find the last index')
        ans[1] = binarySearch(nums,target, False)
    
    return ans


def binarySearch(nums,target,first):
    ans = -1
    start, end = 0, len(nums)-1

    while(start<=end):
        mid = start + (end-start)//2
        print('start mid end ',start,mid,end)

        if(nums[mid]>target):
            end = mid-1
            print('mid is greater than target ', start, end)
        elif(nums[mid]<target):
            start = mid+1
            print('mid is less than target ', start, end)
        else:
            ans = mid
            print('target == mid', start, mid, end)
            if(first):
                print('while true ans start end',ans, start, end)
                end = mid-1
                print('while true start end',start, end)

            else:
                print('while false ans start end',ans,start, end)
                start = mid+1
                print('while false start end',start, end)

    return ans

# nums = [5,7,7,8,8,10] 
# target = 8
# target = 6
nums = [] 
target = 0
print(searchRange(nums,target))


        