# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def widthOfBinaryTree(self, root):
        maxwidth = 0
        depthCounter = {}
        bfsQueue = collections.deque()
        bfsQueue.append([root, 0, 0])
        while len(bfsQueue) > 0:
            node, depth, index = bfsQueue.popleft()
            if depth not in depthCounter:
                if depth != 0:
                    width = max(depthCounter[depth-1]) - min(depthCounter[depth-1]) + 1
                    if width > maxwidth:
                        maxwidth = width
                depthCounter[depth] = []
            if node is None:
                continue
            else:
                depthCounter[depth].append(index)
                bfsQueue.append([node.left, depth+1, 2*index])
                bfsQueue.append([node.right, depth+1, 2*index+1])

        return maxwidth

        # for entry in depthCounter:
        #     for element in depthCounter[entry]:
        #         if element != 'Null':
        #             start = element
        #             break
        #     for element in reversed(depthCounter[entry]):
        #         if element != 'Null':
        #             end = element
        #             break
        #     depthCounter[entry] = end - start + 1

        # return max(depthCounter.values())