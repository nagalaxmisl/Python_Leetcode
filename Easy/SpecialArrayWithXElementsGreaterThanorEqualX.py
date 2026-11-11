class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums)

        while left <= right:

            count = 0

            mid = (left + right) // 2

            for num in nums:

                if num > mid:
                    count += 1

            if count == mid:
                return mid

            elif count > mid:
                left = mid + 1

            else:
                right = mid - 1

        return -1

solution = Solution()

print(solution.specialArray([3,5]))
print(solution.specialArray([0,0]))
print(solution.specialArray([0,4,3,0,4]))