class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.dfs(nums, [], ans)
        return ans
    
    def dfs(self, nums, path, ans):   
        ans.append(list(path))
        for j in range(len(nums)):
            self.dfs(nums[j+1:], path + [nums[j]], ans)
