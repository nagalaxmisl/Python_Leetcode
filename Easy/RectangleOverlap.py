class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (
            rec1[2] <= rec2[0] or
            rec1[0] >= rec2[2] or
            rec1[3] <= rec2[1] or
            rec1[1] >= rec2[3]
        )

sol = Solution()
print(sol.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))
print(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))
print(sol.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))
