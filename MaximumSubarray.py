class Solution(object):
    def maxSubArray(self, nums):
        globalsum = float('-inf')
        localsum = 0
        for element in nums:
            localsum = max(element,element + localsum)
            globalsum = max(globalsum, localsum)
        return globalsum
        