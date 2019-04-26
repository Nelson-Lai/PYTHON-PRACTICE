# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def helper(numList):
            if numList == []:
                return
            maxNumber = max(numList)
            maxIndex = numList.index(maxNumber)
            leftSubarray = numList[0:maxIndex]
            rightSubarray = numList[maxIndex+1:]

            node = TreeNode(maxNumber)
            node.left = helper(leftSubarray)
            node.right = helper(rightSubarray)
            return node

        return helper(nums)