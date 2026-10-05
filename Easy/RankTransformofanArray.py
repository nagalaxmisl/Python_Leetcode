class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        sorted_arr = sorted(arr)

        rank = {}

        rank_num = 1

        for num in sorted_arr:
            if num not in rank:
                rank[num] = rank_num
                rank_num += 1

        result = []

        for num in arr:
            result.append(rank[num])

        return result

sol = Solution()

print(sol.arrayRankTransform([40,10,20,30]))
print(sol.arrayRankTransform([100,100,100]))
print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))