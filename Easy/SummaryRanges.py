class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            j = i+1

            while j < n and nums[j] == nums[j-1] + 1:
                j += 1

            end = nums[j-1]

            res.append(str(start) if start == end else f"{start}->{end}")
            i = j
        return res

    def main(self):
        print(self.summaryRanges(nums = [0,1,2,4,5,7]))
        print(self.summaryRanges(nums = [0,2,3,4,6,8,9]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()