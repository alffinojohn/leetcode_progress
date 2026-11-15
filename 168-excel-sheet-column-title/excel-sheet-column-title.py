class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = []

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            letters.append(chr(ord('A')+remainder))
            columnNumber //= 26

        return ''.join(reversed(letters))

