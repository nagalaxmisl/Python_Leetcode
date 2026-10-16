

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter

        lucky = -1

        count = Counter(arr)

        for i in range(len(arr)):
            if arr[i] == count[arr[i]]:
                lucky = max(lucky, arr[i])

        return lucky

sol = Solution()

print(sol.findLucky([2,2,3,4]))
print(sol.findLucky([1,2,2,3,3,3]))
print(sol.findLucky([2,2,2,3,3]))

