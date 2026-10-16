class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = [0] * 128
        check = [0] * 128
        for ch in t:
            need[ord(ch)] += 1

        required = len(set(t))   
        have = 0
        left = 0
        best = float('inf')
        best_left = 0

        for i in range(len(s)):
            c = ord(s[i])
            if need[c] > 0:
                check[c] += 1
                if check[c] == need[c]:
                    have += 1

            while have == required:
                if i - left + 1 < best:
                    best = i - left + 1
                    best_left = left

                l = ord(s[left])
                if need[l] > 0:
                    check[l] -= 1
                    if check[l] < need[l]:
                        have -= 1
                left += 1

        if best == float('inf'):
            return ""
        return s[best_left : best_left + best]