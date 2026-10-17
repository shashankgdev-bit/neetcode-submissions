class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def getSubsets(i, temp):
            nonlocal result

            if i < 0:
                result.append(temp)
                return

            getSubsets( i-1, temp)
            getSubsets( i-1, temp + [nums[i]])


            return
        
        getSubsets(len(nums)-1, [])

        return result