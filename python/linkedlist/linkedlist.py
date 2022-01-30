# Implementation of various operation in linked list
# Author: Diamond Mohanty
# Date: 25-Jan-2022

class _Node():
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next: _Node = next

class NodeNotFound(Exception):
    pass

class EmptyList(Exception):
    pass

class ListIndexOutOfBound(Exception):
    pass

class _LinkedListBase():
    def __init__(self) -> None:
        self._header = _Node(None, None) # Sentinel
        self._trailer = _Node(None, None) # Sentinel
        self._header.next = self._trailer
        self._size = 0

    def _is_empty(self) -> bool:
        return self._size == 0

    def __len__(self):
        return self._size

    def _insert_between(self, val, predecessor, successor) -> None:
        '''Inserts a node between to nodes'''
        new_node = _Node(val, successor)
        predecessor.next = new_node
        self._size += 1

    def _remove_node(self, node, predecessor):
        '''Removes a node'''
        if self._is_empty():
            raise EmptyList('List is empty')
        predecessor.next = node.next
        node.next = node.val = None
        self._size -= 1

    def __repr__(self) -> str:
        repr = ''
        head = self._header.next
        while head.next:
            repr += 'Node(val: {}) -> '.format(head.val)
            head = head.next
        return repr.rstrip(' -> ')

class LinkedList(_LinkedListBase):
    def insert(self, val, pos = None):
        '''Inserts at a given position. If position is not given or greater than the number 
        of elements inserts at the end'''        
        predecessor = self._header
        successor = self._header.next
        count = 0
        while successor.next:
            if pos == count:
                self._insert_between(val, predecessor, successor)
                return
            count += 1
            successor = successor.next
            predecessor = predecessor.next

        # Position is not given so insert at last
        self._insert_between(val, predecessor, self._trailer)

    def remove(self, val):
        '''Removes an element
        Raises exception if element not found
        '''
        predecessor = self._header
        current = self._header.next
        while current:
            if current.val == val:
                self._remove_node(current, predecessor)
                current = predecessor.next
            else:
                current = current.next
                predecessor = predecessor.next

    def element_at(self, pos):
        '''Returns the element at a given position
        Raises exception if the position is greater than the number of elements
        '''
        head = self._header.next
        count = 0
        if pos > self._size - 1:
            raise ListIndexOutOfBound('List index out of Bounds')
        while head.next:
            if pos == count:
                return head.val
            count += 1
            head = head.next

# Driver code
new_list = LinkedList()
new_list.insert(1)
new_list.insert(2)
new_list.insert(6)
new_list.insert(3)
new_list.insert(4)
new_list.insert(5)
new_list.insert(6)
print(new_list)
new_list.remove(6)
print(new_list)

    