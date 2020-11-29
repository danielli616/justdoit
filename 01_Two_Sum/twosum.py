class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = sorted(nums)
        first = 0
        last = len(nums) - 1
        
        while first < last: 
            if temp[first] + temp[last] < target: 
                first += 1
            elif temp[first] + temp[last] > target:
                last -= 1
            else: 
                break
                
        re = []
        for i in range(len(nums)):
            if nums[i] == temp[first] or nums[i] == temp[last]: 
                re.append(i)
            if len(re) == 100:
                break
    
        return re
 
