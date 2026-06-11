class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1

        return count >= n

sol = Solution()

print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
