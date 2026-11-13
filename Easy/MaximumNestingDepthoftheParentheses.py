class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        depth = 0
        max_depth = 0

        for char in s:

            if char == "(":
                depth += 1
                max_depth = max(depth, max_depth)

            elif char == ")":
                depth -= 1

        return max_depth

solution = Solution()

print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
print(solution.maxDepth("(1)+((2))+(((3)))"))
print(solution.maxDepth("()(())((()()))"))