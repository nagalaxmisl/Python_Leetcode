class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = 0
        min_sum = 0

        for num in nums:

            total += num
            min_sum = min(min_sum, total)

        return 1-min_sum

solution = Solution()

print(solution.minStartValue([-3,2,-3,4,2]))
print(solution.minStartValue([1,2]))
print(solution.minStartValue([1,-2,-3]))