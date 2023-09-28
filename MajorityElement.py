def majorityElement(nums):
    hmap = {}
    res,maxCount = 0,0

    for n in nums:
        hmap[n] = 1 + hmap.get(n,0)
        if hmap[n] > maxCount:
            res = n
        else:
            res
        maxCount = max(hmap[n],maxCount)
    return res

nums = [1,1,2,2,2,3,3,4,5,6]
print(majorityElement(nums))