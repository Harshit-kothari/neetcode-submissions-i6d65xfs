class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minbuy = prices[0]

        for i in prices:
            maxp = max(maxp, i-minbuy)
            minbuy = min(minbuy, i)
        return maxp
