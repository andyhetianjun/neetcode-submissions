# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lA, lB, = headA, headB 
        while lA != lB:
            lA = lA.next if lA else headB
            lB = lB.next if lB else headA

        
        return lA
