class Solution(object):
    def isValidBST(self, root):
        
        def valid(root,minn,maxx):
            if root is None:
                return True
            
            if not (root.val > minn and root.val < maxx):
                return False
            
            return valid(root.left,minn,root.val) and valid(root.right,root.val,maxx)
            
        return valid(root,float("-inf"),float("inf"))

class Solution2(object):
    def isValidBST(self, root):
        result = []
        result = self.inorder_traversal(root, result)
            
        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                return False
        return True

        
    def inorder_traversal(self,root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.val)
            self.inorder_traversal(root.right, result)
        return result