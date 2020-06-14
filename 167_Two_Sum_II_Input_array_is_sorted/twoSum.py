class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        D = {}
        
        for i in range(len(numbers)):
            val = target - numbers[i] 
            if val in D:
                return [D[val] + 1, i + 1]
            D[numbers[i]] = i;