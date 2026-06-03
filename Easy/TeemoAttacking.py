class Solution:

    def findPoisonedDuration(self, timeSeries, duration):

        if not timeSeries:
            return 0

        total = 0

        for i in range(len(timeSeries) - 1):

            gap = timeSeries[i + 1] - timeSeries[i]

            total += min(duration, gap)

        total += duration

        return total

sol = Solution()

print(sol.findPoisonedDuration([1,4], 2))
print(sol.findPoisonedDuration([1,2], 2))