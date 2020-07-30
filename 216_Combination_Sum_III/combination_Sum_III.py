class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 9:
            nums = list(range(1, n + 1))
        else:
            nums = list(range(1, 10))
            
        res = []
        
        self.dfs(nums, k, n, [], res)
        
        return res
        
        
    def dfs(self, nums, k, target, path, res):
                
        if target  < 0 or len(path) > k:
            return     

        if target  == 0 and len(path) == k:
            res.append(path)
            
        for j in range(len(nums)):
            self.dfs(nums[j+1:], k, target - nums[j], path + [nums[j]], res)
        