# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
         
        def nodeRecurse(node):
            if node is None:
                return
            nodeRecurse(node.left)
            if len(nodeList) == k:
                return
            nodeList.append(node.val)
            nodeRecurse(node.right)
        
        nodeList = []
        nodeRecurse(root)
        print(nodeList)
        return nodeList[k-1]


'''
100
|
5
|\
1 6
   \
    7
     \
      8
'''