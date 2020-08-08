class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        marked = [False] * len(nums)
        self.dfs(nums, [], marked, ans, )
        return ans
    
    def dfs(self, nums, path, marked, ans):      
        if len(path) == len(nums):
            ans.append(list(path))
            return
            
        for i, n in enumerate(nums):
            if marked[i]:
                continue
            if i > 0 and nums[i] == nums[i -1] and not marked[i - 1]:
                continue   
            marked[i] = True
            path.append(n)
    
            self.dfs(nums, path, marked, ans)
        
            path.pop()
            marked[i] = False