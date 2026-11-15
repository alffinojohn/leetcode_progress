class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        exp = len(columnTitle) - 1
        total = 0

        for letter in columnTitle:
            total += (ord(letter) - ord('A') + 1) * (26 ** exp)
            exp -= 1

        return total





        