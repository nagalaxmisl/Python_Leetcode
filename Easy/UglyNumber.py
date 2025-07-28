class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1

    def main(self):
        print(self.isUgly(n=6))
        print(self.isUgly(n=1))
        print(self.isUgly(n=14))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
