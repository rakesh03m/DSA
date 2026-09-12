# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = head
        
        while (ls and ls.next):
            if (ls.val == ls.next.val):
                ls.next = ls.next.next
            else:
                ls = ls.next

        return head
