# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set() # We can also use list[] but it has an time complexity of o(n^2)
        current=head
        while current:
            if current in seen:
                return True
            seen.add(current)
            current=current.next
        return False