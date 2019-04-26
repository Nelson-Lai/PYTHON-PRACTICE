# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):

        def isValidSubtree(node):

            if node is None:
                return False

            isLeft = isValidSubtree(node.left)
            if isLeft == False:
                node.left = None
            isRight = isValidSubtree(node.right)
            if isRight == False:
                node.right = None
            if node.val == 0 and isLeft == False and isRight == False:
                return False
            else:
                return True

        isValidSubtree(root)
        return root
