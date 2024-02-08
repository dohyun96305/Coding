# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Maxiumum Depth of Binary Tree
# Tree 구조 리스트의 가장 깊은 깊이 return 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None : 
            return 0

        left_depth = self.maxDepth(root.left) # 재귀함수 
        right_depth = self.maxDepth(root.right)            

        return 1 + max(left_depth, right_depth)  