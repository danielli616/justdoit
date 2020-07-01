class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        array = [i for i in range(1, n + 1)]
        res = []
        for i in range(len(array)):
            path = []
            self.dfs(i, array, path, res, k)   
        return res
        
        
    
    def dfs(self, index, nums, path, res, k):
        path.append(nums[index])
        if len(path) == k:
            res.append(path[:])
        for j in range(index + 1, len(nums)):
            self.dfs(j, nums, path, res, k)    
        path.pop()
            
    