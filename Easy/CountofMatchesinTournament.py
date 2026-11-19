class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """

        total_matches = 0

        while n > 1:

            matches = n // 2
            total_matches += matches

            if n % 2 == 0:
                n = n // 2

            else:
                n = (n // 2) + 1

        return total_matches

solution = Solution()

print(solution.numberOfMatches(7))
print(solution.numberOfMatches(14))