class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y

        return bin(xor).count('1')

    def main(self):
        print(self.hammingDistance(x = 1, y = 4))
        print(self.hammingDistance(x=3, y=1))

if __name__ == "__main__":
    sol = Solution()
    sol.main()