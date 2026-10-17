class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr != self.tail:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        left = self.head
        right = self.head.next
        new = ListNode(val)
        left.next = new
        right.prev = new
        new.next = right
        new.prev = left


    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        right = self.tail
        left = self.tail.prev
        left.next = new
        right.prev = new
        new.next = right
        new.prev = left

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        curr = self.head.next
        while curr != self.tail and i < index:
            curr = curr.next
            i += 1
        if i != index:
            return 
        new = ListNode(val)
        right = curr
        left = curr.prev
        right.prev = new
        left.next = new
        new.prev = left
        new.next = right

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head.next
        while curr != self.tail and i < index:
            curr = curr.next
            i += 1
        if curr == self.tail:
                return
        if i != index:  
            return 
        right = curr.next
        left = curr.prev
        left.next = right
        right.prev = left

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)