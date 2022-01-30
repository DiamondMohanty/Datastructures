---
layout: post
title:  "Positional List in Python"
---

# Positional List

**Code**
```python
class _Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next: _Node = None
        self.prev: _Node = None

    def __repr__(self) -> str:
        return 'Node(prev: {}, val: {}, next: {})'.format(self.prev, self.val, self.next)


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
        new_node.next = successor
        new_node.prev = predecessor
        self.size += 1
        return new_node

    def _delete_node(self, node: _Node) -> any:
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        ele = node.val
        node.prev = node.next = node.val = None
        self.size -= 1
        return ele


class PostionList(_DoublyLinkedBase):

    class Position():
        def __init__(self, container, node) -> None:
            self._container = container
            self._node: _Node = node

        def element(self):
            return self._node.val

        def __eq__(self, __o) -> bool:
            return type(__o) is type(self) and self._node is __o.node

        def __ne__(self, __o) -> bool:
            return not (self == __o)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise ValueError('p is not a position type')        
        elif p._container is not self:
            raise ValueError('p does not belong to this positional list')
        elif p._node.next is None and p._node != self.trailer:
            raise ValueError('p is invalidated')
        return p._node

    def _make_position(self, node):
        if node is self.header or node is self.trailer: # Sentinel
            return None
        else:
            return self.Position(self, node)

    # ---- Accessors ---- #
    def first(self) -> Position:
        return self._make_position(self.header.next)

    def last(self) -> Position:
        return self._make_position(self.trailer.prev)

    def before(self, p) -> Position:
        node = self._validate(p)
        return self._make_position(node.prev)
    
    def after(self, p) -> Position:
        node = self._validate(p)
        return self._make_position(node.next)

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> any:
        cursor = self.first()
        while cursor:
            yield cursor.element()
            cursor = self.after(cursor)

    
    # ---- Mutators ---- #
    def _insert_between(self, val, predecessor: _Node, successor: _Node) -> None:
        node = super()._insert_between(val, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e: any):
        return self._insert_between(e, self.header, self.header.next)

    def add_last(self, e: any):
        return self._insert_between(e, self.trailer.prev, self.trailer)
        

    def add_after(self, e: any, pos: Position):
        node = self._validate(pos)
        return self._insert_between(e, node, node.next)

    def add_before(self, e: any, pos: Position):
        node = self._validate(pos)
        return self._insert_between(e, node.prev, node)

    def delete(self, p: Position):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, old: Position, new: any):
        old_node = self._validate(old)
        value = old_node.val
        old_node.val = new
        return value

if __name__ == '__main__':
    # Driver Code
    pList = PostionList()
    p = pList.add_last(8)
    print(pList.last().element())
    q = pList.add_after(5, p)
    print(pList.before(q).element())
    r = pList.add_before(3, q)
    print(r.element())
    print(pList.after(p).element())
    print(pList.before(p))
    s = pList.add_first(9)
    print(pList.delete(pList.last()))
    print(pList.replace(p, 7))
```

