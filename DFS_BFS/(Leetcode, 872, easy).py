# https://leetcode.com/problems/leaf-similar-trees/description/
# Leaf-Similar Trees
# 두 트리구조 그래프의 leaf 리스트가 같은지 확인

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        root1leaf = []
        root2leaf = []

        self.checkleaf(root1, root1leaf) 
        self.checkleaf(root2, root2leaf)

        return root1leaf == root2leaf
        

    def checkleaf(self, root, temp) : # DFS 
        
        if not root : 
            return # 더이상 노드가 없을 경우 X
        
        if not root.left and not root.right : 
            temp.append(root.val) # leaf-value : 자식 노드가 없는 노드, temp에 저장

        else : 
            self.checkleaf(root.left, temp) # 재귀 함수
            self.checkleaf(root.right, temp) # 재귀 함수