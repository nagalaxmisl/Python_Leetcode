class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """

        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')

        return command

solution = Solution()

print(solution.interpret("G()(al)"))
print(solution.interpret("G()()()()(al)"))
print(solution.interpret("(al)G(al)()()G"))