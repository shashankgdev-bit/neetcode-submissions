class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, x in enumerate(nums):
            check = target - x
            if check in d:
                return [d[check],i]
            d[x]=i
