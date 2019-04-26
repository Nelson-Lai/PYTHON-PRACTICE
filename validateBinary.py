# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def isValidSubtree(node,currentmin,currentmax):
            if node is None:
                return True
            
            if node.val >= currentmax or node.val <= currentmin:
                return False
            
            isLeft = isValidSubtree(node.left, currentmin, node.val)
            isRight = isValidSubtree(node.right, node.val, currentmax)
            if isLeft and isRight:
                return True
            else:
                return False
        return isValidSubtree(root, -math.inf, math.inf)