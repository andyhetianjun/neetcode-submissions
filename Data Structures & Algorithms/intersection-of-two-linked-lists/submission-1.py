# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        countA = 0
        curr = headA
        while curr:
            countA += 1 
            curr = curr.next

        countB = 0
        curr = headB
        while curr:
            countB += 1 
            curr = curr.next
        currA = headA
        currB = headB
        if countA > countB:
            for i in range(countA - countB):
                currA = currA.next
        
        elif countB > countA: 
            for i in range(countB - countA):
                currB = currB.next
        
        while currA:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None

