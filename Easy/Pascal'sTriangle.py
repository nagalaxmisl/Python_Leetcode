class Solution(object):
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result


if __name__ == "__main__":
    sol = Solution()

    print("Test 1:", sol.generate(5))
    print("Test 2:", sol.generate(1))