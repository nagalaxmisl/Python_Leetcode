class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        expected_sum = n * (n + 1) // 2

        actual_sum = sum(nums)

        return (expected_sum - actual_sum)

    def main(self):
        print(self.missingNumber(nums = [3,0,1]))
        print(self.missingNumber(nums = [0,1]))
        print(self.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()