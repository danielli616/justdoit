# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ans = [False]
        
        self.dfs(root, [], sum, ans)
        
        return ans[0]
    
    
    def dfs(self, root, path, target, ans):
    
        if not root:
            return
        
        path.append(root.val)
        
        if not root.left and not root.right:
            if sum(path) == target:
                ans[0] = True
        
        self.dfs(root.left, path, target, ans)          
        self.dfs(root.right, path, target, ans)

        path.pop()
        