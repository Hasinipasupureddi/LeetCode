# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge case: empty list or single node
        if not head:
            return head
        current = head
        # Traverse the list until the second-to-last node
        while current and current.next:
            if current.val == current.next.val:
                # Duplicate found! Skip the next node
                current.next = current.next.next
            else:
                # No duplicate, move the pointer forward
                current = current.next    
        return head