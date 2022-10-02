class CashNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next= None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.updateMostRecent(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print('put')
        if key in self.dict:
            node = self.dict[key]
            node.val = value
        else:
            if len(self.dict) == self.capacity:
                del self.dict[self.head.key]
                self.removeHead()
                
            node = CashNode(key, value)
            self.dict[key] = node
        
        self.updateMostRecent(node)
        
        
    def updateMostRecent(self, node):
        if self.head and self.head.key == node.key:
            self.removeHead()
        
        if self.tail and not self.tail.key == node.key:
            if node.prev:
                node.prev.next = node.next
            if node.next:    
                node.next.prev = node.prev
            
            node.next = None
            self.tail.next = node
            node.prev = self.tail
        
        self.tail = node
        
        if not self.head:
            self.head = node
        
        
    def removeHead(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)