class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        return (nums[-1] - 1) * (nums[-2] - 1)

solution = Solution()

print(solution.maxProduct([3,4,5,2]))
print(solution.maxProduct([1,5,4,5]))
print(solution.maxProduct([3,7]))