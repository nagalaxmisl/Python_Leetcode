# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         number = ""
#         for i in range(len(digits)):
#             str_number = str(digits[i])
#             number += str_number
#
#         plus_one = str(int(number) + 1)
#
#         plus_one_arr = []
#         for i in range(len(plus_one)):
#             plus_one_arr.append(plus_one[i])
#
#         return plus_one_arr

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If all digits were 9 (e.g., [9, 9, 9])
        return [1] + digits

    def main(self):
        print(self.plusOne(digits = [1,9,9]))
        print(self.plusOne(digits = [4,3,2,1]))
        print(self.plusOne(digits = [9]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()