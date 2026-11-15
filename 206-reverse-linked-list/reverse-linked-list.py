# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        temp = head

        while temp:
            rest = temp.next
            temp.next = dummy
            dummy = temp
            temp = rest

        return dummy



        