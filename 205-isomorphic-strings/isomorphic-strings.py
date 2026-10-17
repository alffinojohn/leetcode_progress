class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matching_s = {}
        matching_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in matching_s:
                if matching_s[s[i]] != t[i]:
                    return False

            if t[i] in matching_t:
                if matching_t[t[i]] != s[i]:
                    return False

            matching_s[s[i]] = t[i]
            matching_t[t[i]] = s[i]


        return True

        