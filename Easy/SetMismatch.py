class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        duplicate = sum(nums) - sum(set(nums))

        missing = n * (n+1) // 2 - sum(set(nums))

        return [duplicate, missing]

sol = Solution()

print(sol.findErrorNums([1,2,2,4]))

print(sol.findErrorNums([1,1]))