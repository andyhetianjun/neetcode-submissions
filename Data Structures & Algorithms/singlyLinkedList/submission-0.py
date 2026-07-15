class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for j in range(index):
            if curr is None:
                return -1
            curr = curr.next 
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_Node = Node(val)
        if self.head is None:
            self.head = new_Node
            return
        curr = self.head
        while (curr.next != None) :
            curr = curr.next
        curr.next = new_Node
        

    def remove(self, index: int) -> bool:
        curr = self.head
        if curr is None:
            return False
        if index == 0:
            self.head = self.head.next 
            return True
        for j in range (index - 1):
            curr = curr.next
            if curr is None:
                return False
        if curr.next is None: 
            return False
        curr.next = curr.next.next 
            
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while (curr is not None):
            values.append(curr.val)
            curr = curr.next

        return values

        
