class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        length = 0
        l = 0
        r = 0

        while r < len(s):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            length = max(length, r-l+1)

            letters.add(s[r])
            r += 1

        return length



            


        