class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maximum = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            maximum = max(maximum, right - left + 1)

        return maximum
