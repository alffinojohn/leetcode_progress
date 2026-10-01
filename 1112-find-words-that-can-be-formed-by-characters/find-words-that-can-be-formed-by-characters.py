class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        res = 0


        for word in words:
            count = Counter(chars)
            flag = True

            for ch in word:
                if count[ch] <= 0:
                    flag = False
                    break

                count[ch] -= 1
            if flag:
                res += len(word)

        return res




        