# Circular Queue implementation using array
# Author: Diamond Mohanty
# Date: 08-Jan-2022

class EmptyQueue(Exception):
    pass

class CircularQueue():

    def __init__(self) -> None:
        self._n = 2 # Size of the queue
        self._data = self._n * [None]
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueue(self, element) -> None:
        
        if self._front == self._n - 1: # Full condition
            # Resizing the queue
            self._n *= 2 
            temp = self._data
            self._data = [None] * self._n
            for idx in range(len(temp)):
                self._data[idx] = temp[idx]
            
        self._data[self._front] = element
        self._size += 1
        self._front = (self._front + 1) % self._n
            

    def dequeue(self) -> any:
        if self._front == self._rear:
            raise EmptyQueue('Queue is empty')
        else:
            ele = self._data[self._rear]
            self._data[self._rear] = None
            self._rear = (self._rear + 1) % self._n
            self._size -= 1
            return ele

    def __len__(self) -> int:
        return self._size

# Testing Code
elements = [1,2,3,4]
queue = CircularQueue()
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


