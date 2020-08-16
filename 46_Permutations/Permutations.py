class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """  
        ans = []
        marked = [False] * len(nums)
        self.dfs(nums, [], marked, ans)
        return ans
    
    def dfs(self, nums, path, marked, ans):    
        if len(path) == len(nums):
            ans.append(list(path))
            return
            
        for i, n in enumerate(nums):
            if marked[i]:
                continue
            marked[i] = True
            path.append(n)

            self.dfs(nums, path, marked, ans)
            
            path.pop()
            marked[i] = False

def main():
    s = Solution()
    nums = [1,2,3]
    ans = s.permute(nums)
    print(ans)

if __name__ == "__main__":
    main()

