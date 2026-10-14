# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and slow:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            slow = slow.next
            if not fast or not slow:
                return False
            if fast.val == slow.val:
                return True

        return False