class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        if k > len(nums):
            return 0

        maxSum = 0
        totalSum = 0
        distinct = set()
        l = 0
        for i in range(len(nums)):
            while (l < len(nums) and nums[i] in distinct) or i-l+1 > k:
                distinct.remove(nums[l])
                totalSum -= nums[l]
                l += 1

            distinct.add(nums[i])
            totalSum += nums[i]


            if i-l+1 == k:
                maxSum = max(maxSum, totalSum)

        return maxSum



            







        