class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        a, b = 1, 2

        for i in range(3, n + 1):
            a, b = b, a + b
        return b

    def main(self):
        print(self.climbStairs(n=2))
        print(self.climbStairs(n=4))

if __name__ == "__main__":
    sol = Solution()
    sol.main()