class Solution(object):
    def kthSmallest(self, root, k):
        nums= []
        
        def inordertraversal(root,nums=[]):
            if root is None:
                return None

            inordertraversal(root.left,nums)
            if len(nums) == k:
                return
            nums.append(root.val)
            inordertraversal(root.right,nums)
        inordertraversal(root,nums)
        return nums[-1]

class Solution2(object):
    def kthSmallest(self, root, k):
        nums1 = self.inordertraversal(root,nums=[])
        return nums1[k-1]
        
    
    def inordertraversal(self,root,nums=[]):
        if root is None:
            return None
        self.inordertraversal(root.left,nums)
        nums.append(root.val)
        self.inordertraversal(root.right,nums)
        return nums