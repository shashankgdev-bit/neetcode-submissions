class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        i = 0

        for x in nums:
            check = target - x
            if check in d:
                return [d[check],i]
            d[x]=i
            i += 1 