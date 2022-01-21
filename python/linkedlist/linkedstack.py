# Implementation of stack using linked list
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

class LinkedStack():
    def __init__(self) -> None:
        self.linkedlist = _LinkedList()
        self.size = 0

    def push(self, ele) -> None:
        '''Adds a new element to the stack
        @params
        ele(any): The element to be added
        '''
        new_node = _Node(ele)
        # Inserting to the head of the list
        head = self.linkedlist.head
        new_node.next = head
        self.linkedlist.head = new_node
        self.size += 1

    def pop(self) -> any:
        '''Removes the first inserted element from the stack
        @returns any
        Raises EmptyException if the stack is empty
        '''
        if self.linkedlist.head is None:
            raise EmptyException()
        
        ele = self.linkedlist.head
        self.linkedlist.head = ele.next
        self.size -= 1
        return ele.val

    def __len__(self) -> int:
        '''Returns the number of elements in the stack'''
        return self.size

# Driver Code
stack = LinkedStack()
stack.push(10)
stack.push(11)
print(stack.pop())
print('Length {0}'.format(len(stack)))
stack.push(12)
print(stack.pop())
print(stack.pop())
print(stack.pop()) # This will raise an exception
