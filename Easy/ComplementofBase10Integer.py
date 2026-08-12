class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]

        result = ""

        for b in binary:
            if b == "0":
                result += "1"

            else:
                result += "0"

        return int(result, 2)

sol = Solution()

print(sol.bitwiseComplement(n = 5))
print(sol.bitwiseComplement(n = 7))
print(sol.bitwiseComplement(n = 10))