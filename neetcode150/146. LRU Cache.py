class ListNode:
    #class for Nodes to be mapped in cache map
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    #1, n
    def __init__(self, capacity: int):
        self.cpcty = capacity
        self.cache = {} #map key2nodes
        #left: LRU right:MRU
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        #linking the two so that new nodes can be inserted in b/w
    
    #remove node from left
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        
    #insert node at right
    def insert(self,node):
        prv, nxt = self.right.prev, self.right
        prv.next, nxt.prev = node, node
        node.prev, node.next = prv, nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #remove it from cache from left
            self.insert(self.cache[key]) #insert it in cache from right
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #remove from left
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key]) #insert at right
                        
        if len(self.cache) > self.cpcty:
            lru = self.left.next #get the least recently used node
            self.remove(lru) #remove node from left
            del self.cache[lru.key] #remove node from hashMap

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)