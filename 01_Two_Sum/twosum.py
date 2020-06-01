class Solution(object):
  def twoSum(self, nums, target):
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

    return [nums.index(temp[first]), nums.index(temp[last])]
