class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        max_l = 0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l += 1

            window.add(s[i])
            length = i-l+1
            max_l = max(max_l, length)

        return max_l

        




            
                



        
        



            

        