class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = (1 << num.bit_length()) - 1
        return num ^ mask

    def main(self):
        print(self.findComplement(num=5))
        print(self.findComplement(num=1))

if __name__ == "__main__":
    sol = Solution()
    sol.main()