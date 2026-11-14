class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window = set()
        l = 0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l += 1

            window.add(s[i])
            length = i-l+1
            max_length = max(max_length, length)


        return max_length




            
                



        
        



            

        