# Implementation of circular queue using linked list
# Author: Diamond Mohanty
# Date: 25-Jan-2022

class _Node():
    def __init__(self, ele) -> None:
        self.next: _Node = None
        self.val = ele

class EmptyException(Exception):
    pass

class CircularLinkedList():
    def __init__(self) -> None:
        self.current: _Node = None
        self._size = 0

    def enqueue(self, element) -> None:
        '''Inserts a new element to the queue
        @params:
        element (any) - New element for the list
        '''
        new_node = _Node(element)
        if self._size == 0: # Empty Queue
            new_node.next = new_node
        else:
            new_node.next = self.current.next
            self.current.next = new_node
        self.current = new_node
        self._size += 1

    def first(self) -> any:
        '''Returns the first element of the queue without removing it
        '''
        if self._size == 0:
            raise EmptyException('Queue is empty')

        return self.current.next.val

    def dequeue(self) -> any:
        '''Returns the first element from the list and removes it
        '''
        if self._size == 0:
            raise EmptyException('Queue is empty')

        ele = self.current.next
        self.current.next = ele.next
        self._size -= 1
        return ele.val

    def rotate(self) -> None:
        '''Changes the first element to the last of the queue
        '''
        if self._size == 0:
            return
        self.current = self.current.next
        

    def __len__(self) -> int:
        '''Returns the size of the queue
        '''
        return self._size


# Driver Code
queue = CircularLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print('Size: ', len(queue))
print('First: ', queue.first())
queue.rotate()
print('First: ', queue.first())
queue.rotate()
print('First: ', queue.first())
