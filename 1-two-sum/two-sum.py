class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        newNum = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in newNum:
                return [newNum[diff], i]

            newNum[num] = i
       