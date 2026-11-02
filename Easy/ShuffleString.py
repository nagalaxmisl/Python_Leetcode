class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        result = [""] * len(s)

        for i in range(len(s)):

            result[indices[i]] = s[i]

        return "".join(result)

solution = Solution()

print(solution.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(solution.restoreString(s = "abc", indices = [0,1,2]))