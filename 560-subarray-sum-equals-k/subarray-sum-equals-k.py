class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0:1}

        total = 0
        ans = 0

        for num in nums:
            total += num

            diff = total - k

            if diff in sums:
                ans += sums[diff]
            sums[total] = sums.get(total, 0) + 1

        return ans








        



        