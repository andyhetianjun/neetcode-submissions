# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next

        l, r = 0, len(array) - 1

        while l < r:
            if array[l] == array[r]:
                l += 1
                r -= 1 
            else:
                return False
        return True
         