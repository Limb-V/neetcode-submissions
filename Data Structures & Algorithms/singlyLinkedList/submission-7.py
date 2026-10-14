class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next    

class LinkedList:
    
    def __init__(self):
        self.l_list = []
        self.head = None
        self.tail = None
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return (-1)
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail is None:
            self.head = new_node
        else:
            prev = self.tail
            prev.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        curr = self.head
        if index == 0:
            if curr == None:
                return False
            elif curr.next == None:
                self.head = None
                self.tail = None
                return True
            else:
                self.head = curr.next
                return True
        i = 0
        while curr and i < index - 1:   
            curr = curr.next
            i += 1

        if curr is None or curr.next is None:   
            return False

        if curr.next == self.tail:      
            self.tail = curr

        curr.next = curr.next.next            
        return True

    def getValues(self) -> List[int]:
        my_list = []
        curr = self.head
        while curr:
            my_list.append(curr.val)
            curr = curr.next
        return my_list
