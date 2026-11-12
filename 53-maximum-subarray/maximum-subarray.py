class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        l = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0


            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)

        return max_sum
            

            
