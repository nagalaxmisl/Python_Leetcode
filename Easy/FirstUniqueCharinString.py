class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        freq = Counter(s)

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1

    def main(self):
        print(self.firstUniqChar(s = "leetcode"))
        print(self.firstUniqChar(s = "loveleetcode"))
        print(self.firstUniqChar(s="aabb"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()