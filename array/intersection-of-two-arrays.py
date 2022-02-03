def intersection(nums1, nums2):
    # return list(set(nums1) & set(nums2))
    map1 = {}
    ret = []
    for i in nums1:
        map1[i] = 1
    
    for j in nums2:
        if j in map1 and map1[j] == 1:
            ret.append(j)
            map1[j] = 0
    return ret
            