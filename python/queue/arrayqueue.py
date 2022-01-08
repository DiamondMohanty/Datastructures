# Basic Implementation of Queue datastructure using array
# Author: Diamond Mohanty
# Date: 08-Jan-2022

class EmptyQueue(Exception):
    pass

class ArrayQueue():
    def __init__(self) -> None:
        self._data = []
        self._front = 0
        self._rear = 0

    def enqueue(self, element) -> None:
        self._data.append(element)
        self._front += 1

    def dequeue(self) -> any:
        if self.is_empty():
            raise EmptyQueue('Queue is empty')

        element = self._data[self._rear]
        self._rear += 1
        return element
            

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        if self._front == self._rear:
            return True
        return False

# Testing Code
elements = [1,2,3,12]
queue = ArrayQueue()
for ele in elements:
    queue.enqueue(ele)

queue.dequeue()
queue.dequeue()
queue.enqueue(5)
queue.enqueue(7)
print('Queue Size', len(queue))

try:
    while True:
        print(queue.dequeue(), end=' ')
except EmptyQueue:
    pass

