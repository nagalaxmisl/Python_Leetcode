class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """

        count = 0

        for i in range(len(arr)-m):

            if arr[i] == arr[i+1]:
                count += 1

            else:
                count = 0

            if count >= k:
                return True

        return False

solution = Solution()

print(solution.containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3))
print(solution.containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2))
print(solution.containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3))

