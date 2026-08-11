# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tempArr = []
        for lst in lists:
            while lst :
                tempArr.append(lst.val)
                lst = lst.next
            
        tempArr.sort()
        res = ListNode(0)
        temp =res
        for i in tempArr:
            temp.next = ListNode(i)
            temp = temp.next
        return res.next
