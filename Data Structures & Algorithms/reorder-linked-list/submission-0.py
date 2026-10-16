# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 1 2 3 4 5 6
        # 0 1 2 3  6 5 4
        # 0 6 1 5 2 4 3

        # find mid
        fast, slow = head, head
        while fast and fast.next and fast.next.next and slow:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # reverse half
        prev = None
        curr = mid.next
        mid.next = None 
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt        

        # merge two list
        dummy = ListNode()
        tail = dummy
        while head and prev:
            tail.next = head
            head = head.next
            tail = tail.next
            tail.next = prev
            prev = prev.next
            tail = tail.next
        tail.next = head or prev
        head = dummy.next

