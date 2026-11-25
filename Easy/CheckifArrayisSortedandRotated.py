class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        count = 0

        for i in range(n):

            if nums[i] > nums[(i+1)%n]:
                count += 1

        return count <= 1

solution = Solution()

print(solution.check([3,4,5,1,2]))
print(solution.check([2,1,3,4]))
print(solution.check([1,2,3]))