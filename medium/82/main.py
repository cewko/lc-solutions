class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        prev, current = dummy_node, head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                prev.next = current
            else:
                prev = prev.next
                current = current.next

        return dummy_node.next

            

