class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
    
        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums)):         
            if nums[i] >= target:
                return i