class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)

sol = Solution()

print(sol.largestSumAfterKNegations(nums = [4,2,3], k = 1))
print(sol.largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))
print(sol.largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))