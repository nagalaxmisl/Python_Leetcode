class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for num in nums:
            digits = len(str(num))

            if digits % 2 == 0:
                count += 1

        return count

sol = Solution()

print(sol.findNumbers(nums = [12,345,2,6,7896]))
print(sol.findNumbers(nums = [555,901,482,1771]))