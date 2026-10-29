class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0

        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    result += 1

        return result

solution = Solution()

print(solution.numIdenticalPairs([1,2,3,1,1,3]))
print(solution.numIdenticalPairs([3,3,3,3]))
print(solution.numIdenticalPairs([1,2,3]))