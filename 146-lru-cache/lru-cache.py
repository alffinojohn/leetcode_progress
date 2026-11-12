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

    def _remove(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    def _add(self, node):
        before = self.tail.prev

        before.next = node
        node.prev = before

        node.next = self.tail
        self.tail.prev = node

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
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

            if len(self.cache) > self.size:
                oldest = self.head.next
                self._remove(oldest)
                del self.cache[oldest.key]






        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)