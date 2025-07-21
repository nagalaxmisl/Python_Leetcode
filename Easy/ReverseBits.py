class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_n = bin(n)[2:].zfill(32)
        reverse_binary = binary_n[::-1]

        reverse_decimal = int(reverse_binary,2)

        return reverse_decimal

    def main(self):
        print(self.reverseBits(n = 43261596))
        print(self.reverseBits(n = 2147483644))


if __name__ == "__main__":
    sol = Solution()
    sol.main()