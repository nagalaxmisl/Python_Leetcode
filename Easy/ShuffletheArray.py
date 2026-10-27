class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])

        return result

solution = Solution()

print(solution.shuffle(nums = [2,5,1,3,4,7], n = 3))
print(solution.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(solution.shuffle(nums = [1,1,2,2], n = 2))