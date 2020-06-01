class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = nums[:]
        temp.sort()
        first = 0
        length = len(nums)
        last = length - 1
        
        while True: 
            if temp[first] + temp[last] < target: 
                first += 1
            elif temp[first] + temp[last] > target:
                last -= 1
            else:
                break
                
        re = []
        i = 0
        while True:
            print(nums[i])
            if nums[i] == temp[first] or nums[i] == temp[last]: 
                re.append(i)
            if len(re) == 2:
                break
            i += 1 
    
        return re
        
        
        
