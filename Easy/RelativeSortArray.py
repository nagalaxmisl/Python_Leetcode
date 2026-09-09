class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        from collections import Counter

        count = Counter(arr1)

        result = []

        for num in arr2:
            if num in count:
                result.append([num] * count[num])
                del count[num]

        remaining = sorted(count.keys())

        for num in remaining:
            result.append([num] * count[num])

        return result

solution = Solution()

print(solution.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(solution.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))