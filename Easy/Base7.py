class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        result = []

        while num > 0:
            result.append(str(num%7))
            num //= 7

        base7 = ''.join(reversed(result))

        return '-'+base7 if negative else base7

    def main(self):
        print(self.convertToBase7(num=100))
        print(self.convertToBase7(num=-7))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
