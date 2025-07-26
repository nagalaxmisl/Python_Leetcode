class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total

        return num

    def main(self):
        print(self.addDigits(num = 38))
        print(self.addDigits(num=0))

if __name__ == "__main__":
    sol = Solution()
    sol.main()