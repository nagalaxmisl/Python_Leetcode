# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head


    def main(self):
        print(self.deleteDuplicates(head = [1,1,2]))
        print(self.deleteDuplicates(head = [1,1,2,3,3]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()