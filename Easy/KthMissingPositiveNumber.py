class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        right = len(arr)-1

        while left <= right:

            mid = (left+right)//2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1

            else:
                right = mid - 1

        return left + k

solution = Solution()

print(solution.findKthPositive(arr = [2,3,4,7,11], k = 5))
print(solution.findKthPositive(arr = [1,2,3,4], k = 2))