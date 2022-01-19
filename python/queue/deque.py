# Dequeue implementation using circular array
# Author: Diamond Mohanty
# Date: 08-Jan-2022

class EmptyQueue(Exception):
    pass

class Deque():
    def __init__(self) -> None:
        self._size = 0
        self._data = [None] * 2
        self._front = 0


    def __len__(self) -> None:
        return self._size

    def first(self) -> any:
        return self._data[self._front]

    def last(self) -> any:
        last = (self._size - self._front) % len(self._data) 
        return self._data[last]

    def add_first(self, e) -> None:
        if self._size == len(self._data):
            # Queue is full increase the size of underlying list
            self._resize_(len(self._data) * 2)
            
        self._data[self._front] = e
        self._front = (self._front - 1) % len(self._data)
        self._size += 1

    def add_last(self, e) -> None:
        if self._size == len(self._data):
            # Queue is full increase the size of underlying list
            self._resize_(len(self._data) * 2)

        self._data[self._front] = e
        self._front = (self._front + 1) % len(self._data)
        self._size += 1

    def remove_last(self) -> any:
        last = (self._size - self._front) % len(self._data) 
        item = self._data[last]
        self._data[last] = None
        self._size -= 1
        return item

    def remove_first(self) -> any:
        item = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        return item

    def _resize_(self, cap) -> None:
        temp = self._data
        self._data = [None] * cap
        walk = self._front
        for idx in range(self._size):
            self._data[idx] = temp[walk]
            walk = (walk + 1) % len(temp)
        self._front = 0

    def is_empty(self) -> bool:
        return self._size == 0


# Testing Code
dq = Deque()
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