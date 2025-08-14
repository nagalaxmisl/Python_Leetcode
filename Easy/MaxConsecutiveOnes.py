class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        ans = 0

        for x in nums:
            if x == 1:
                curr += 1

                if curr > ans:
                    ans = curr

            else:
                curr = 0

        return ans

    def main(self):
        print(self.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
        print(self.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
