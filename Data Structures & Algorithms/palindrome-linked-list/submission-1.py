# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.curr = head

        def recurse(node):
            if node is not None:
                if not recurse(node.next):
                    return False
                if self.curr.val != node.val:
                    return False
                self.curr = self.curr.next
            return True

        return recurse(head)
            