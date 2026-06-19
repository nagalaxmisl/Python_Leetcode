class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)

        for i, num in enumerate(nums):
            if num == largest:
                continue

            if largest < 2 * num:
                return -1

        return nums.index(largest)

sol = Solution()

print(sol.dominantIndex([3,6,1,0]))
print(sol.dominantIndex([1,2,3,4]))