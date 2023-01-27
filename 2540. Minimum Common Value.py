def getCommon(nums1, nums2):
    if nums1[0]==nums2[0] :
        return nums1[0]
    
    one,two= 0,0
    
    while(True):

        if one==len(nums1)-1 or two==len(nums2):
            return -1
        
        if nums1[one]<nums2[two]:
            one += 1
        elif nums2[two]<nums1[one]:
            two += 1
        else :
            return nums1[one]