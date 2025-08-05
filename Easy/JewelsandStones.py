class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        seen = jewels
        count = 0

        for char in stones:
            if char in seen:
                count += 1

        return count

    def main(self):
        print(self.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
        print(self.numJewelsInStones(jewels = "z", stones = "ZZ"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()