# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        head = ListNode(0)
        tail = head

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2 + carry
            carry = total // 10

            node = ListNode(total % 10)
            tail.next = node
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next
        