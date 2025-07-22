class Solution(object):
    # def hammingWeight(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     binary_n = (bin(n)[2:])
    #     count = 0
    #
    #     for i in range(len(binary_n)):
    #         if binary_n[i] == '1':
    #             count += 1
    #
    #     return count
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

    def main(self):
        print(self.hammingWeight(n = 11))
        print(self.hammingWeight(n=128))
        print(self.hammingWeight(n=2147483645))

if __name__ == "__main__":
    sol = Solution()
    sol.main()