class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def checkSum(i, temp, target):
            nonlocal result

            if i < 0:
                return

            if target < 0:
                return

            if target == 0:
                result.append(temp)
                return 

            checkSum(i-1, temp, target)
            checkSum(i, temp + [nums[i]], target-nums[i])

            return 

        checkSum(len(nums)-1, [], target)

        return result