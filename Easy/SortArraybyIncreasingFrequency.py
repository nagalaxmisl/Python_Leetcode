class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        from collections import Counter

        freq = Counter(nums)

        nums.sort(key = lambda x: (freq[x], -x))

        return nums

solution = Solution()

print(solution.frequencySort([1,1,2,2,2,3]))
print(solution.frequencySort([2,3,1,3,2]))
print(solution.frequencySort([-1,1,-6,4,5,-6,1,4,1]))