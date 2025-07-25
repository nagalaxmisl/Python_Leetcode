class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1

    def main(self):
        print(self.isPowerOfThree(n=27))
        print(self.isPowerOfThree(n=0))
        print(self.isPowerOfThree(n=-1))

if __name__ == "__main__":
    sol = Solution()
    sol.main()