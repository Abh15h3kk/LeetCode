def removeDuplicates(nums):
        nodups = []
        for i in nums:
            if i not in nodups:
                nodups.append(i)
        return nodups

def removeDuplicate(nums):
    nums[:] = sorted(set(nums))
    return nums

def removeDups(nums):
      visited = {}
      for i in nums:
        visited[i] = True
      return list(visited.keys)

def removeDuplicatess(arr):
  visited = {}
  for element in arr:
    visited[element] = True
  return list(visited.keys())

num = [1,2,2,3,3,4,4,5,6,7,7,8]
print(removeDuplicatess(num))
     
