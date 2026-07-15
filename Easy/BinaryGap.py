class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]

        previous = -1
        answer = 0

        for i in range(len(binary)):
            if binary[i] == '1':
                if previous != -1:

                    answer = max(answer, i - previous)

                previous = i

        return answer

sol = Solution()

print(sol.binaryGap(22))
print(sol.binaryGap(8))