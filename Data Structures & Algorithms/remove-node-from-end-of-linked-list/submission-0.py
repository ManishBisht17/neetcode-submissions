# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        ans = head

        # Move curr n steps ahead
        for _ in range(n):
            curr = curr.next

        # Edge case: remove head
        if curr is None:
            return head.next

        # Move both pointers
        while curr.next:
            curr = curr.next
            ans = ans.next

        # Remove node
        ans.next = ans.next.next

        return head
        