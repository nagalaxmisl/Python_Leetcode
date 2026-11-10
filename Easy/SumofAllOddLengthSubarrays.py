class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = 0
        n = len(arr)

        for i in range(n):
            for j in range(i, n):

                if (j - i + 1) % 2 != 0:
                    total += sum(arr[i:j + 1])

        return total

solution = Solution()

print(solution.sumOddLengthSubarrays([1,4,2,5,3]))
print(solution.sumOddLengthSubarrays([1,2]))
print(solution.sumOddLengthSubarrays([10,11,12]))