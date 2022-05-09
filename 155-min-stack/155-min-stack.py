class StackNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.min = float('inf')
        
class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        node = StackNode(val)
        node.min = min(val, self.headMin())
        node.next = self.head
        self.head = node

    def pop(self) -> None:
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def top(self) -> int:
        if not self.head:
            return None
        return self.head.val

    def getMin(self) -> int:
        return self.headMin()
        
    def headMin(self):
        if not self.head:
            return float('inf')
        return self.head.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()