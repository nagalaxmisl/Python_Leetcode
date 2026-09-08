class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

solution = Solution()

print(solution.defangIPaddr("1.1.1.1"))
print(solution.defangIPaddr("255.100.50.0"))