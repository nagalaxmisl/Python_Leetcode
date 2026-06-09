class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from collections import Counter

        count = Counter(nums)

        result = 0

        for num in count:
            if num + 1 in count:
                result = max(result, count[num] + count[num + 1])

        return result

sol = Solution()

print(sol.findLHS([1,3,2,2,5,2,3,7]))

print(sol.findLHS([1,2,3,4]))

print(sol.findLHS([1,1,1, 1]))