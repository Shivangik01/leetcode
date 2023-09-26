#store pointers in dict
#can return value

#depends on capacity
#one without capacity
#if exists update

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next= self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        pos = self.cache[key]
        pos.prev.next = pos.next
        pos.next.prev = pos.prev
        
        self.to_end(key)
        return pos.val

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            pos = self.cache[key]
            pos.val = value
            pos.prev.next = pos.next
            pos.next.prev = pos.prev
            self.to_end(key)

        elif len(self.cache)==self.capacity:
            pos = self.head.next

            del self.cache[pos.key]

            self.head.next = pos.next
            pos.next.prev = self.head
            pos.next= None
            pos.prev = None
            node = Node(key,value)
            self.cache[key] = node
            self.to_end(key)

        else:
            node = Node(key,value)
            self.cache[key] = node
            self.to_end(key)
        


    def to_end(self,key):

        pos = self.cache[key]
        pos.next = self.tail
        pos.prev = self.tail.prev
        self.tail.prev.next= pos
        self.tail.prev = pos


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)