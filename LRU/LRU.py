#
#  Common implementation for LRU with Python.
#  However, the doubly linked list implementaton was interesting to implement
#  Both are included here
#
'''
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key):
        if key not in self
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)
'''


class DLNode:

    def __init__(self, key=None, value=None):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value


class LRUCache:
    '''LRU Cache Double Link List implementation.  '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.head.value = 'head'
        self.tail.prev = self.head
        self.tail.value = "tail"
        self.cache = {}

    def print(self):
        node = self.head
        while node:
            print(str(node.value) + "->")
            node = node.next

    def add(self, node):
        '''Add the node the head of the cache'''
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def move_to_head(self, node):
        node.next.prev = node.prev  # remove from list
        node.prev.next = node.next
        self.add(node)

    def get(self, key: int) -> int:
        print("get {}".format(key))
        node = self.cache.get(key)
        if node:
            self.move_to_head(node)
            # self.print()
            print('return {}'.format(node.value))
            return node.value
        print('return -1')
        # self.print()
        return -1

    def evict(self):
        node = self.tail.prev
        print("before evicting {}".format(node.value))
        # self.print()
        node.prev.next = self.tail
        self.tail.prev = node.prev
        node.next = None
        node.prev = None
        del self.cache[node.key]
        del node
        self.size -= 1
        print('after evict with tail {}'.format(self.tail.prev.value))
        # self.print()

    def put(self, key: int, value: int) -> None:
        print("put {}".format(key))
        '''
            Add the item to the LRU cache
            If we are capacity then remove the LRU and add
            other wise just add the item.
        '''

        node = self.cache.get(key)
        if node is None:
            if self.size >= self.capacity:
                self.evict()
            print('Adding new key')
            node = DLNode(key, value)
            self.cache[key] = node
            self.add(node)
            self.size += 1
        else:
            print('key found')
            if node.value != value:
                node.value = value
            self.move_to_head(node)
        # self.print()

