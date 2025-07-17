class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decimal_sum = int(a,2) + int(b, 2)

        binary_sum = bin(decimal_sum)[2:]

        return binary_sum

    def main(self):
        print(self.addBinary(a = "11", b = "1"))
        print(self.addBinary(a = "1010", b = "1011"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
