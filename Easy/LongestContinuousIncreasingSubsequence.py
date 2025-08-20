class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_len = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
                max_len = max(current, max_len)

            else:
                current = 1

        return max_len

    def main(self):
        print(self.findLengthOfLCIS(nums = [1,3,5,4,7]))
        print(self.findLengthOfLCIS(nums = [2,2,2,2,2]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()