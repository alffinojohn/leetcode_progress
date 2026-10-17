class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(sorted(nums))
        longest = 0

        for num in new_nums:
            length = 0
            if num - 1 in new_nums:
                continue
            else:
                while num in new_nums:
                    length += 1
                    num += 1

                longest = max(longest, length)

        return longest
                


            



                        
            
