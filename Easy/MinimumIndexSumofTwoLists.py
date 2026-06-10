class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list2_map = {word:i for i,word in enumerate(list2)}

        result = []

        min_sum = float('inf')

        for i, word in enumerate(list1):
            if word in list2_map:
                index_sum = i + list2_map[word]

                if index_sum < min_sum:
                    min_sum = index_sum
                    result.append(word)

                elif index_sum == min_sum:
                    result.append(word)

        return result

sol = Solution()

print(sol.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))

print(sol.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))

print(sol.findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))