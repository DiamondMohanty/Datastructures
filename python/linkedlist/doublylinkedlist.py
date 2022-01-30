# Abstraction of Doubly Linked list
# Author: Diamond Mohanty
# Date: 25-Jan-2022

class _Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next: _Node = None
        self.prev: _Node = None


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
        predecessor.next = new_node
        successor.prev = new_node
        new_node.prev = predecessor
        new_node.next = successor
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

