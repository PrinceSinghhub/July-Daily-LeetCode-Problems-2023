class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class DoublyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, key, val):
        node = Node(key, val)
        if self.tail != None:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.tail = self.head = node
        self.size += 1
        return node

    def remove(self, mp):
        if self.head:

            del mp[self.head.key]
            if self.head == self.tail:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
            self.size -= 1


    def move_to_front(self, node):
        if not self.head or not node or node == self.tail:
            return
        if self.size == 1:
            return
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next


class LRUCache:
    def __init__(self, size):
        self.size = size
        self.list = DoublyList()
        self.hasmap = {}

    def get(self, key):
        if not self.hasmap.get(key):
            return -1
        node = self.hasmap[key]
        self.list.move_to_front(node)
        return node.val

    def put(self, key, val):
        if self.hasmap.get(key):
            self.hasmap[key].val = val
            self.list.move_to_front(self.hasmap[key])
            return
        self.hasmap[key] = self.list.insert(key, val)
        if self.list.size > self.size:
            self.list.remove(self.hasmap)