class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        take, not_take = nums[0], 0

        for i in range(1, len(nums)):
             take, not_take =  not_take + nums[i], max(take, not_take)

        return max(take, not_take)
