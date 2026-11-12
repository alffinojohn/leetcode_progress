class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        l = 0
        max_out = 0

        for i in range(len(s)):
            char_freq[s[i]] = char_freq.get(s[i], 0) + 1
            length = sum(char_freq.values())
            
            while length - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l += 1
                length -= 1

            max_out = max(max_out, length)

        return max_out

            



        