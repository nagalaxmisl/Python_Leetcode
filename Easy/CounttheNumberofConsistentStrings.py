class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        allowed_set = set(allowed)

        count = 0

        for word in words:

            consistent = True

            for ch in word:
                if ch not in allowed_set:
                    consistent = False
                    break

            if consistent:
                count += 1

        return count

solution = Solution()

print(solution.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(solution.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(solution.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))