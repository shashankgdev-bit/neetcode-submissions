class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0]*26
        window = [0]*26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        left = 0

        for right in range(len(s1),len(s2)):
            if need == window:
                return True
            
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[left]) - ord('a')] -= 1

            left += 1

        return need == window
 
