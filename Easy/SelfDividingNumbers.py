class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def is_self_dividing(n):
            x = n

            while x > 0:
                d = x % 10

                if d == 0 or n % d != 0:
                    return False

                else:
                    x = x // 10

            return True

        ans = []

        for num in range(left, right + 1):
            if is_self_dividing(num):
                ans.append(num)

        return ans

    def main(self):
        print(self.selfDividingNumbers(left = 1, right = 22))
        print(self.selfDividingNumbers(left=47, right=85))

if __name__ == "__main__":
    sol = Solution()
    sol.main()