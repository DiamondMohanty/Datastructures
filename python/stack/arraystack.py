# Implemention of Stack using array and adapter design pattern
# Author: Diamond Mohanty
# Date: 05-Jan-2022

class Empty(Exception):
    pass

class ArrayStack():
    def __init__(self) -> None:
        """ Creates a new stack of infinite capacity
        """
        self._items = []

    def __len__(self):
        """Returns the number of elements in the stack
        """
        return len(self._items)

    def push(self, item) -> None:
        """Adds the given item to the stack
        """
        self._items.append(item)

    def pop(self):
        """Removes the top most item from the stack and returns it
        Raise Empty exception when the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._items.pop()
    
    def is_empty(self) -> bool:
        """Checks if the stack is empty
        Return True if empty
        """
        return len(self._items) == 0

    def top(self):
        """Returns the topmost element from the stack without removing it
        """
        return self._items[-1]
    

# Test Code
if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(5)
    stack.push(7)
    print(len(stack))
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(stack.pop())