class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """

        arr = [first]

        for num in encoded:

            next_num = arr[-1] ^ num
            arr.append(next_num)

        return arr

solution = Solution()

print(solution.decode(encoded = [1,2,3], first = 1))
print(solution.decode(encoded = [6,2,7,3], first = 4))