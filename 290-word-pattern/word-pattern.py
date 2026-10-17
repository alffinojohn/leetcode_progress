class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        matching = {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            if pattern[i] in matching:
                if matching[pattern[i]] != words[i]:
                    return False
                else:
                    continue

            if words[i] in matching.values():
                return False

            matching[pattern[i]] = words[i]

        return True





        