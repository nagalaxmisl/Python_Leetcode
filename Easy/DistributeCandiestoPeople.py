class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """

        result = [0] * num_people

        remaining = candies
        i = 0
        give = 1

        while remaining > 0:
            amount = min(give, remaining)

            result[i] += amount
            remaining -= amount

            give += 1
            i += 1

            if i == num_people:
                i = 0

        return result

solution = Solution()

print(solution.distributeCandies(candies = 7, num_people = 4))
print(solution.distributeCandies(candies = 10, num_people = 3))
