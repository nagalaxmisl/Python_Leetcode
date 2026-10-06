class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        arr.sort(key=lambda x: (bin(x).count('1'), x))

        return arr

sol = Solution()

print(sol.sortByBits([0,1,2,3,4,5,6,7,8]))

print(sol.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))