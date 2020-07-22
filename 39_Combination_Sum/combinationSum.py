class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        for i in range(len(candidates)):
            path = []
            self.dfs(i, candidates, target, path, res)
        
        return res
        
        
    def dfs(self, index, nums, target, path, res):
             
        if (target - nums[index]) < 0:
            return     
        
        path.append(nums[index])  
        
        if(target - nums[index]) == 0:
            res.append(path[:])

        for j in range(index, len(nums)):
            self.dfs(j, nums, target - nums[index], path, res)
        
        path.pop()