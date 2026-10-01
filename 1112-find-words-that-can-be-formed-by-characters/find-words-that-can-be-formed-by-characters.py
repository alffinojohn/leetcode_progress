class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        res = 0
        count = Counter(chars)



        for word in words:
            available = count.copy()
            flag = True

            for ch in word:
                if available[ch] <= 0:
                    flag = False
                    break

                available[ch] -= 1
            if flag:
                res += len(word)

        return res




        