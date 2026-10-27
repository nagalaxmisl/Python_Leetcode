class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result

solution = Solution()

print(solution.runningSum([1,2,3,4]))
print(solution.runningSum([1,1,1,1,1]))
print(solution.runningSum([3,1,2,10,1]))