class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = {}
        best = 0

        for left in range(len(s) - minSize + 1):
            sub = s[left:left+minSize]

            if len(set(sub)) <= maxLetters:
                counts[sub] = counts.get(sub, 0) + 1
                best = max(best, counts[sub])

        return best

        