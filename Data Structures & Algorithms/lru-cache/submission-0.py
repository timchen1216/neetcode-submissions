class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node        

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        node = self.kv[key]
        self._remove(node)
        self._add_front(node)
        return node.val        

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self._remove(self.kv[key])
        node = Node(key, value)
        self.kv[key] = node
        self._add_front(node)
        if len(self.kv) > self.cap:
            lru = self.tail.prev          
            self._remove(lru)
            del self.kv[lru.key]          
        
