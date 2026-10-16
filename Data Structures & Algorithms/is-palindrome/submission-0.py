class Solution:
    def isPalindrome(self, s: str) -> bool:
        parts = []

        for c in s:
            if(c.isalnum()):
                parts.append(c.lower())

        return parts == parts[::-1]