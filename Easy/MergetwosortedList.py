# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

    def print_list(self, node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    def main(self):
        def build_linked_list(lst):
            dummy = ListNode(0)
            current = dummy
            for val in lst:
                current.next = ListNode(val)
                current = current.next
            return dummy.next

        l1 = build_linked_list([1, 2, 4])
        l2 = build_linked_list([1, 3, 4])
        merged = self.mergeTwoLists(l1, l2)
        self.print_list(merged)

        l1 = build_linked_list([])
        l2 = build_linked_list([])
        merged = self.mergeTwoLists(l1, l2)
        self.print_list(merged)

        l1 = build_linked_list([])
        l2 = build_linked_list([0])
        merged = self.mergeTwoLists(l1, l2)
        self.print_list(merged)

if __name__ == "__main__":
    sol = Solution()
    sol.main()
