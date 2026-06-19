class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i

            left_sum += nums[i]

        return -1

sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))
print(sol.pivotIndex([1,2,3]))
print(sol.pivotIndex([2,1,-1]))