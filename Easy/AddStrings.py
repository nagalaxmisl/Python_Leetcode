class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum = int(num1) + int(num2)
        return str(sum)

    def main(self):
        print(self.addStrings(num1 = "11", num2 = "123"))
        print(self.addStrings(num1 = "456", num2 = "77"))
        print(self.addStrings(num1 = "0", num2 = "0"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()