'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res = []
        
        def dfs(root, parent, lvl):
            if root:
                if root.val == x:
                    res.append((parent, lvl))
                if root.val == y:
                    res.append((parent, lvl))
                    
                dfs(root.left, root, lvl + 1)
                dfs(root.right, root, lvl + 1)
        
        dfs(root, None, lvl=0)
        
        x_res, y_res = res
        
        if x_res[0] != y_res[0] and x_res[1] == y_res[1]:
            return True
        
        return False  