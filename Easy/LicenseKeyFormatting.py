class Solution:

    def licenseKeyFormatting(self, s, k):

        cleaned = s.replace('-', '')

        groups = []

        i = len(cleaned)

        while i > 0:
            start = max(0, i - k)

            groups.append(cleaned[start:i])

            i -= k

        groups.reverse()

        return '-'.join(groups)

sol = Solution()

print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(sol.licenseKeyFormatting("2-5g-3-J", 2))