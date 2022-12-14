def intersect(nums1, nums2):
    l1,l2 = len(nums1), len(nums2)
    res = []
   

    if(l1<l2):
        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2.remove(num)
        print(res)
    else:
        for num in nums2:
            if num in nums1:
                res.append(num)
                nums1.remove(num)
        print(res)

    return res

nums1 = [1,2,2,1] 
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1=[1,2,2,1]
nums2=[2]
nums1=[1,2]
nums2=[1,1]
intersect(nums1,nums2)