class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat

        flat = []

        for row in mat:
            for num in row:
                flat.append(num)

        result = []

        for i in range(0, len(flat), c):
            result.append(flat[i:i+c])

        return result

if __name__ == "__main__":
    sol = Solution()

    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4

    print(sol.matrixReshape(mat, r, c))