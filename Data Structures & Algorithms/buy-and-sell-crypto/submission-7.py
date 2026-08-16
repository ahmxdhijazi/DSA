class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        profit = 0
        smallest_idx = prices.index(min(prices))
        for smallest_idx, price in enumerate(prices):
            for i in range(smallest_idx, len(prices)):
                profit = prices[i] - price

                if profit > largest:
                    largest = profit


        return largest