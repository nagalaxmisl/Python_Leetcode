class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        result = []

        for i in range(len(words)):

            for j in range(len(words)):

                if i != j and words[i] in words[j]:

                    result.append(words[i])
                    break

        return result

sol = Solution()

print(sol.stringMatching(["mass","as","hero","superhero"]))
print(sol.stringMatching(["leetcode","et","code"]))
print(sol.stringMatching(["blue","green","bu"]))