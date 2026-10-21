class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        prev_one = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if prev_one != -1:
                    distance = i - prev_one - 1

                    if distance < k:
                        return False

                prev_one = i

        return True

solution = Solution()

print(solution.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))
print(solution.kLengthApart(nums = [1,0,0,1,0,1], k = 2))