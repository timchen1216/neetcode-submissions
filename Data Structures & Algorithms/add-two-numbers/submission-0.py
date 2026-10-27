# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        curr1, curr2 = l1, l2
        prev = None
        while curr1 or curr2:
            if not curr2:              # l2 用完，把 l1 剩下的接過來當作要寫入的節點
                prev.next = curr1
                curr2, curr1 = curr1, None
            s = curr2.val + (curr1.val if curr1 else 0) + c
            curr2.val = s % 10
            c = s // 10
            prev = curr2
            curr2 = curr2.next
            if curr1:
                curr1 = curr1.next
        if c:
            prev.next = ListNode(1)
        return l2