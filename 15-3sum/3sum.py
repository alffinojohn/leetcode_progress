class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        res = []

        for i in range(len(new_nums)):
            if new_nums[i] > 0:
                exit
            
            if i > 0 and new_nums[i] == new_nums[i-1]:
                continue

            l = i + 1
            r = len(new_nums)-1

            while l < r:
                total = new_nums[i] + new_nums[l] + new_nums[r]

                if total == 0:
                    res.append([new_nums[i], new_nums[l], new_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and new_nums[l] == new_nums[l-1]:
                        l += 1

                    while l < r and new_nums[r] == new_nums[r+1]:
                        r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1


        return res

        