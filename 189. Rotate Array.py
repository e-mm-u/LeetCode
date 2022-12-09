#  naive approach
# def rotate_array(nums, k):
#     arr = [1]*len(nums)
#     print(arr)
#     for i in range(len(nums)):
#         index = (i+k)%len(nums)
#         print(i, index)
#         arr[index] = nums[i]
#     print(arr)
#     return arr

# --------------------------------------------------
#  space complexity O(1) approach, time complexity O(n) approach
def rotate_array(nums,k):
    def reverse(s,e):
        while(s<=e):
            nums[s],nums[e] = nums[e],nums[s]
            s += 1
            e -= 1
    
    l = len(nums)
    k = k%l
    if(l==1 or k==l):
        return
    # reverse the whole array
    reverse(0,l-1)
    # reverse nums[:k]
    reverse(0, k-1)
    # reverse nums[k:]
    reverse(k,l-1)
   
    print(nums)

# nums = [1,2,3,4,5,6,7]
nums = [1,2]

k = 3
rotate_array(nums,k)
# print(rotate_array(nums,k))
