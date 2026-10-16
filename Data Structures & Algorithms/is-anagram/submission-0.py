class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0]*26

        for c,p in zip(s,t):
            count[ord(c) - ord('a')] += 1
            count[ord(p) - ord('a')] -= 1

        for x in count:
            if x != 0:
                return False

        return True