class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        option1 = nums[-1] * nums[-2] * nums[-3]

        option2 = nums[0] * nums[1] * nums[-1]

        return max(option1, option2)

    def main(self):
        print(self.maximumProduct(nums = [1,2,3]))
        print(self.maximumProduct(nums = [1,2,3,4]))
        print(self.maximumProduct(nums = [-1,-2,-3]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()