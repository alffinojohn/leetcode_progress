class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        if capacity > 0:
            self.size = capacity

        self.cache = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        before = self.tail.prev

        before.next = node
        node.prev = before

        node.next = self.tail
        self.tail.prev = node

    def _remove(self,node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add(node)

        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            node = Node(key,value)
            self._add(node)
            self.cache[key] = node

            if len(self.cache) > self.size:
                node = self.head.next
                self._remove(node)
                del self.cache[node.key]

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)