def mergeSort(nums):
    if len(nums)<=1:
        return nums
 
    mid = len(nums)//2

    left = nums[:mid]
    right = nums[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(nums,left,right)

def merge(nums,left,right):
    n = len(left)
    m = len(right)
    i=0
    j=0
    k=0
    while i < n and j < m :
        if left[i] < right[j]:
            nums[k] = left[i]
            i+=1
        else:
            nums[k] = right[j]
            j+=1
        k+=1
    while i<n:
        nums[k] = left[i]
        i+=1
        k+=1
    while j<m:
        nums[k] = right[j]
        j+=1
        k+=1
    return nums

nums = [5,4,3,6,1]
print(mergeSort(nums))