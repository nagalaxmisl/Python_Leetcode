class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = heights[:]

        expected.sort()

        count = 0

        for i in range(len(heights)):
            if heights[i] == expected[i]:
                count += 1

        return count

sol = Solution()

print(sol.heightChecker([1,1,4,2,1,3]))
print(sol.heightChecker([5,1,2,3,4]))
print(sol.heightChecker([1,2,3,4,5]))