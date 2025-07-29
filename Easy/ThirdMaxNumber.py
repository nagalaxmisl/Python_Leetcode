class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_nums = sorted(set(nums), reverse=True)

        if len(distinct_nums) >=3:
            return distinct_nums[2]
        return distinct_nums[0]

    def main(self):
        print(self.thirdMax(nums = [3,2,1]))
        print(self.thirdMax(nums = [1,2]))
        print(self.thirdMax(nums = [2,2,3,1]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()