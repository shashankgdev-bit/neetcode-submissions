class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        maxm = 0

        for x in s:
            if x-1 not in s:
                while x in s:
                    x += 1
                    count += 1
            maxm = max(count,maxm)
            count = 0

        return maxm
        