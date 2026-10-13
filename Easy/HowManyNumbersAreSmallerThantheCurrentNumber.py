class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for num in nums:

            count = 0

            for other in nums:
                if other < num:
                    count += 1

            result.append(count)

        return result

sol = Solution()

print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))

print(sol.smallerNumbersThanCurrent([6,5,4,8]))

print(sol.smallerNumbersThanCurrent([7,7,7,7]))