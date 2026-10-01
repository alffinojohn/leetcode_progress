class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        maxAvg = 0

        for i in range(k):
            total += nums[i]
            maxAvg = total /k

        for i in range(k, len(nums)):
            total -= nums[i-k]
            total += nums[i]
            avg = total /k
            maxAvg = max(maxAvg, avg)

        return maxAvg