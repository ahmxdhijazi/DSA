class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit = 0

        for price in prices:
            smallest = min(smallest, price)

            max_profit = max(max_profit, price-smallest)

        return max_profit