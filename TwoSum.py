def twoSum(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left,right]
            elif nums[left] + nums[right] < target:
                left+=1
            else:
                right-=1
        return False


def twoSum(self, nums, target):
        visited = {}
        for i,n in enumerate(nums):
            if target-n in visited:
                return [visited[target-n],i]
            else:
                visited[n] = i
        return False