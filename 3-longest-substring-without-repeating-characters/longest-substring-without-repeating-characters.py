class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        count = 0
        l = 0

        for i in range(len(s)):
            while s[i] in curr:
                curr.remove(s[l])
                l += 1

            curr.add(s[i])
            count = max(count, i-l+1)

        return count



            

        