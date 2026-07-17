class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False

            elif nums[i] > nums[i + 1]:
                increasing = False

        return increasing or decreasing

sol = Solution()

print(sol.isMonotonic([1,2,2,3]))
print(sol.isMonotonic([6,5,4,4]))
print(sol.isMonotonic([1,3,2]))