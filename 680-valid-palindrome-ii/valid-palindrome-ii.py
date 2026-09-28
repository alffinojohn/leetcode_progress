class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        # Move inward until we find a mismatch
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1

        # Already a palindrome
        if l >= r:
            return True

        # Try deleting the left character
        l_trial = l + 1
        r_trial = r
        left_valid = True

        while l_trial < r_trial:
            if s[l_trial] != s[r_trial]:
                left_valid = False
                break

            l_trial += 1
            r_trial -= 1

        # Try deleting the right character
        l_trial2 = l
        r_trial2 = r - 1
        right_valid = True

        while l_trial2 < r_trial2:
            if s[l_trial2] != s[r_trial2]:
                right_valid = False
                break

            l_trial2 += 1
            r_trial2 -= 1

        return left_valid or right_valid