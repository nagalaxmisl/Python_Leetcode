class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        seen = set()

        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True

            seen.add(num)

        return False

    def main(self):
        print(self.checkIfExist(arr = [10,2,5,3]))
        print(self.checkIfExist(arr = [3,1,7,11]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()