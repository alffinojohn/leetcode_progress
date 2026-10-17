class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        matching_letter = {}
        matching_words = {}


        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            if pattern[i] in matching_letter:
                if matching_letter[pattern[i]] != words[i]:
                    return False

            if words[i] in matching_words:
                if matching_words[words[i]] != pattern[i]:
                    return False

            matching_letter[pattern[i]] = words[i]
            matching_words[words[i]] = pattern[i]

        return True





        