class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_total = nums[0]
        total = 0

        for i in range(len(nums)):
            if total < 0:
                total = nums[i]
            else:
                total += nums[i]

            max_total = max(max_total, total)

        return max_total

            

        
