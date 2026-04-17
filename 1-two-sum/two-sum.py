class Solution(object):
    def twoSum(self, nums, target):
        nummap={}
        for i , num in enumerate(nums):
            complement = target - num
            if complement in nummap:
                return [nummap[complement],i]
            nummap[num] = i 
            



