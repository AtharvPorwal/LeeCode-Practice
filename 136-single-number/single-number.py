class Solution(object):
    def singleNumber(self, nums):
      
        unique_nu = 0

        for id in nums:
            unique_nu ^= id
        return unique_nu
    