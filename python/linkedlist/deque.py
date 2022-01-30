# Deque implementation using Linked List
# Author: Diamond Mohanty
# Date: 25-Jan-2022

class _Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next: _Node = None
        self.prev: _Node = None

class Empty(Exception):
    pass

class _DoublyLinkedBase():
    def __init__(self) -> None:
        self.header = _Node(None)
        self.trailer = _Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def _insert_between(self, val, predecessor: _Node, successor: _Node) -> None:
        new_node = _Node(val)
        new_node.next = successor
        new_node.prev = predecessor
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1

    def _delete_node(self, node: _Node) -> any:
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        ele = node.val
        node.prev = node.next = node.val = None
        self.size -= 1
        return ele


class LinkedDeque(_DoublyLinkedBase):
    def first(self) -> any:
        '''Returns the first element of the list without removing it
        '''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.header.next.val
    
    def last(self) -> any:
        '''Returns the last element of the list without removing it
        '''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.trailer.prev.val
    
    def add_first(self, val) -> None:
        '''Adds an element to the starting of the dequeue
        '''
        successor = self.header.next
        predecessor = self.header
        self._insert_between(val, predecessor, successor)

    def add_last(self, val) -> None:
        '''Adds an element to the ending of the deque
        '''
        successor = self.trailer
        predecessor = self.trailer.prev
        self._insert_between(val, predecessor, successor)

    def remove_last(self) -> any:
        '''Removes the element present at the end of the dequeue
        '''
        if self.is_empty():
            raise Empty('Deque is empty')
        to_remove = self.trailer.prev
        val = self._delete_node(to_remove)
        return val

    def remove_first(self) -> any:
        '''Removes the element present at the starting of the dequeue
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        to_remove = self.header.next
        val = self._delete_node(to_remove)
        return val
    
    def traverse(self):
        node = self.header.next
        while node.next is not None:
            print(node.val, end='->')
            node = node.next


# Driver Code
dq = LinkedDeque()
dq.add_last(5)
dq.add_first(3)
dq.add_first(7)

print(dq.first())
print(dq.remove_last()) 
print(len(dq))
print(dq.remove_last()) 
print(dq.remove_last()) 
dq.add_first(6)
print(dq.last())
dq.add_first(8)
print(dq.is_empty())
print(dq.last())