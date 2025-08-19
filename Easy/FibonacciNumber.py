class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n == 1:
             return 1

        a, b = 0, 1

        for _ in range(2, n+1):
            a, b = b, a+b

        return b

    def main(self):
        print(self.fib(n=2))
        print(self.fib(n=3))
        print(self.fib(n=4))

if __name__ == "__main__":
    sol = Solution()
    sol.main()