class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = []

        for num in nums:
            squares.append(num ** 2)

        squares.sort()

        return squares

    def main(self):
        print(self.sortedSquares(nums = [-4,-1,0,3,10]))
        print(self.sortedSquares(nums = [-7,-3,2,3,11]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
