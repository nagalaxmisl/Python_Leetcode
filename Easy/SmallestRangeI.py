class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return max(0, max(nums) - min(nums) - 2 * k)

sol = Solution()

print(sol.smallestRangeI([1],0))
print(sol.smallestRangeI([0,10],2))
print(sol.smallestRangeI([1,3,6],3))