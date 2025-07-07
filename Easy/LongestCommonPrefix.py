class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    def main(self):
        print(self.longestCommonPrefix(strs=["flower","flow","flight"]))
        print(self.longestCommonPrefix(strs=["dog","racecar","car"]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()

