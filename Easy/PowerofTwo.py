class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n & (n-1)) == 0

    def main(self):
        print(self.isPowerOfTwo(n=1))
        print(self.isPowerOfTwo(n=16))
        print(self.isPowerOfTwo(n=3))

if __name__ == "__main__":
    sol = Solution()
    sol.main()