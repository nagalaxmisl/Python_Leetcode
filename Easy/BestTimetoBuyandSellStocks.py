class Solution(object):
    def maxProfit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit

prices = [7, 1, 5, 3, 6, 4]

solution = Solution()

result = solution.maxProfit(prices)

print("Maximum Profit:", result)