class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """

        result = []

        for i in range(len(prices)):

            discount = 0

            for j in range(i+1, len(prices)):

                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break

            result.append(prices[i] - discount)

        return result

solution = Solution()

print(solution.finalPrices([8,4,6,2,3]))
print(solution.finalPrices([1,2,3,4,5]))
print(solution.finalPrices([10,1,1,6]))