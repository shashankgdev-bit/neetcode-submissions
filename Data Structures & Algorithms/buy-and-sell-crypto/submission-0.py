class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for x in prices:
            minimum = min(minimum,x)
            maximum = max(maximum,x-minimum)

        return maximum
        