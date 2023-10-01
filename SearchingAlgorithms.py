def linearSearch(nums,value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return -1

def binarySearch(nums,value):
    left = 0
    right = len(nums) - 1
    middle = (left+right)//2

    while not (nums[middle] == value) and left<=right:
        if value < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
        middle = (left + right)//2
    if value == nums[middle]:
        return middle
    else:
        return -1

nums = [1,4,5,7,8,9,11]
print(binarySearch(nums,88))





