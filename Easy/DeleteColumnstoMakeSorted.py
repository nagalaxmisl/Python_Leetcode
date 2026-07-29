class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        rows = len(strs)
        cols = len(strs[0])

        count = 0

        for col in range(cols):
            for row in range(rows - 1):
                if strs[row][col] > strs[row + 1][col]:
                    count += 1
                    break

        return count

sol = Solution()

print(sol.minDeletionSize(["cba","daf","ghi"]))
print(sol.minDeletionSize(["a","b"]))
print(sol.minDeletionSize(["zyx","wvu","tsr"]))