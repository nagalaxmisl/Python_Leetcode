class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n==1

    def main(self):
        print(self.isPowerOfFour(n=16))
        print(self.isPowerOfFour(n=5))
        print(self.isPowerOfFour(n=1))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
