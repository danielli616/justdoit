class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        
        return res
        
        
    def dfs(self, nums, target, path, res):
                
        if target  < 0:
            return     

        if target  == 0:
            res.append(path)
            
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            self.dfs(nums[j+1:], target - nums[j], path + [nums[j]], res)
        
            
