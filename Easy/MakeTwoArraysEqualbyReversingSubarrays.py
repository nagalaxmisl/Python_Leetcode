class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """

        from collections import Counter

        return Counter(target) == Counter(arr)

solution = Solution()

print(solution.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3]))
print(solution.canBeEqual(target = [7], arr = [7]))
print(solution.canBeEqual(target = [3,7,9], arr = [3,7,11]))