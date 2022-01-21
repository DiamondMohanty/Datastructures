# Implementation of queue using linked list
# Author: Diamond Mohanty
# Date: 20-Jan-2022

class _Node():
    def __init__(self, val) -> None:
        '''Node class to contain the value and next node information
        @params
        - val(any) : The value of the node
        '''
        self.val = val
        self.next = None

class _LinkedList():
    '''Linked list ADT
    Creates a new empty linked list with no nodes
    '''
    def __init__(self) -> None:
        self.head = None 

class EmptyException(Exception):
    '''Exception class raises when the linked list is empty
    '''
    pass

class LinkedQueue():
    def __init__(self) -> None:
        self.linkedlist = _LinkedList()
        self.size = 0

    def enqueue(self, ele) -> None:
        '''Adds a new element to the queue
        '''
        node = _Node(ele)
        node.next = self.linkedlist.head
        self.linkedlist.head = node
        self.size += 1

    def dequeue(self) -> any:
        '''Removes the first inserted element to the queue
        '''
        if self.linkedlist.head is None:
            raise EmptyException()
        head = self.linkedlist.head
        prev = None
        while head.next is not None:
            prev = head
            head = head.next

        value = None
        if prev is None: # Only one element in the queue
            value = head.val
            self.linkedlist.head = None
        else:
            prev.next = None
            value = head.val

        self.size -= 1
        return value

    def __len__(self):
        '''Returns the number of elements in the queue'''
        return self.size 

# Driver Code
stack = LinkedQueue()
stack.enqueue(10)
stack.enqueue(11)
print(stack.dequeue())
print('Length {0}'.format(len(stack)))
stack.enqueue(12)
print(stack.dequeue())
print(stack.dequeue())
print(stack.dequeue()) # This will raise an exception