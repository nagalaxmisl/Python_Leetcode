class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while  n > 0:
                total += (n % 10) ** 2
                n //= 10
            n = total

        return n == 1

    def main(self):
        print(self.isHappy(n = 19))
        print(self.isHappy(n=2))

if __name__ == "__main__":
    sol = Solution()
    sol.main()