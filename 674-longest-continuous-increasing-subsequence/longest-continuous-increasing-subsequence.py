class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        j = 1
        res = 1
        while j < len(nums):
            while j < len(nums) and nums[j] > nums[j-1]:
                j += 1
            res = max(res, j-i)
            i = j 
            j += 1

        return res




        