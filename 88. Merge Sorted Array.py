def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    n,m,end = n-1,m-1, m+n-1
    
    while m>0 and n>0 :
        
        if nums2[n]>nums1[m]:
            nums1[end] = nums2[n]
            n -= 1
        else:
            nums1[end] = nums1[m]
            m -= 1
        
        end -= 1