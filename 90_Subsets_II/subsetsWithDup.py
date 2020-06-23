class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        res = []
        res.append([])
        mark = [False]*len(nums)
        for i in range(len(nums)):
            path = []
            self.dfs(i, nums, mark, path, res)
        
        return res
            
    
    def dfs(self, index, nums, mark, path, res):
        if index > 0 and nums[index] == nums[index -1] and not mark[index - 1]:
            return   
        mark[index] = True
        path.append(nums[index])
        res.append(path[:])
        for j in range(index + 1, len(nums)):
            self.dfs(j, nums, mark, path, res)    

        path.pop()
        mark[index] = False