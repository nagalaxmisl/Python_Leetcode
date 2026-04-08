class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return float(max_sum) / k

    def main(self):
        print(self.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
        print(self.findMaxAverage(nums = [5], k = 1))

if __name__ == "__main__":
    sol = Solution()
    sol.main()