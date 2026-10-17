class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or not s1:
            return False

        count1 = Counter(s1)

        l = 0
        r = 0
        word = ""

        while r < len(s1):
            word += s2[r]
            r += 1

        count2 = Counter(word)

        while r < len(s2):
            if count1 == count2:
                return True

            count2[s2[l]] -= 1
            count2[s2[r]] = count2.get(s2[r], 0) + 1

            l += 1
            r += 1

        if count1 == count2:
                return True

        return False
        

            










        