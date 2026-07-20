class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1

        while left < right:

            if nums[left] % 2 == 0:
                left += 1

            elif nums[right] % 2 == 1:
                right -= 1

            else:
                nums[left], nums[right] = nums[right], nums[left]

        return nums

sol = Solution()

print(sol.sortArrayByParity([3,1,2,4]))
print(sol.sortArrayByParity([0]))