class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26

        for i in s:
            # Converts the character to its corresponding index (a=0, b=1, ..., z=25)
            chars[ord(i) - 97] += 1

        for i in t:
            # Uses the same index mapping to decrease the character count
            chars[ord(i) - 97] -= 1

        for count in chars:
            if count != 0:
                return False

        return True
