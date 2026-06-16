class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if op == 'C':
                stack.pop()

            elif op == 'D':
                stack.append(stack[-1] * 2)

            elif op == '+':
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(op))

        return sum(stack)

sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))
print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
print(sol.calPoints(["1","C"]))