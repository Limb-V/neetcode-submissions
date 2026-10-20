class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        left = self.tail.prev
        right = self.tail
        new = ListNode(value)
        new.next = right
        new.prev = left
        left.next = new
        right.prev = new

    def appendleft(self, value: int) -> None:
        left = self.head
        right = self.head.next
        new = ListNode(value)
        new.next = right
        new.prev = left
        right.prev = new
        left.next = new

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        removed = self.tail.prev
        self.tail.prev = removed.prev
        removed.prev.next = self.tail
        return removed.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        removed = self.head.next
        self.head.next = removed.next
        removed.next.prev = self.head
        return removed.val