class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        right = 0
        maximum = 0

        while left <= right and right < len(s):

            if(s[right] in chars):
                chars.remove(s[left])
                left += 1

            else:
                chars.add(s[right])
                right += 1
            
            maximum = max(maximum,len(chars))

        return maximum


        