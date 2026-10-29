class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles

        while empty >= numExchange:

            newBottles = empty // numExchange

            empty = empty % numExchange

            total += newBottles
            empty += newBottles

        return total


solution = Solution()

print(solution.numWaterBottles(numBottles = 9, numExchange = 3))
print(solution.numWaterBottles(numBottles = 15, numExchange = 4))