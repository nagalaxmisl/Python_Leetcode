class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def build(string):
            stack = []

            for ch in string:
                if ch == '#':
                    if stack:
                        stack.pop()

                else:
                    stack.append(ch)

            return "".join(stack)

        return build(s) == build(t)

sol = Solution()
print(sol.backspaceCompare(s = "ab#c", t = "ad#c"))
print(sol.backspaceCompare(s = "ab##", t = "c#d#"))
print(sol.backspaceCompare(s = "a#c", t = "b"))