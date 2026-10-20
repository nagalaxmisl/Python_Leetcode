class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)

        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)

            else:
                result.append(False)

        return result

solution = Solution()

print(solution.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(solution.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(solution.kidsWithCandies(candies = [12,1,12], extraCandies = 10))