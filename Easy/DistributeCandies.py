class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique_types = len(set(candyType))

        allowed = len(candyType) // 2

        return min(unique_types, allowed)

sol = Solution()

print(sol.distributeCandies([1,1,2,2,3,3]))
print(sol.distributeCandies([1,1,2,3]))