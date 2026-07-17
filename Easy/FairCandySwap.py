class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        diff = (alice_total - bob_total) // 2  #diff = a - b

        bob_set = set(bobSizes)

        for a in aliceSizes:
            if a-diff in bob_set:
                return [a, a-diff]

sol = Solution()
print(sol.fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))
print(sol.fairCandySwap(aliceSizes = [1,2], bobSizes = [2,3]))
print(sol.fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))