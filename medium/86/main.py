class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        tail_left, tail_right = left, right

        while head:
            if head.val < x:
                tail_left.next = head
                tail_left = tail_left.next
            else:
                tail_right.next = head
                tail_right = tail_right.next

            head = head.next

        tail_left.next = right.next
        tail_right.next = None

        return left.next
        