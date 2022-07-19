class KthLargest:
    #(n-k)logn, n
    #popping elements is a logn ops for heap
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k #prefixing self to make variables work in both funcs
        heapq.heapify(self.minHeap) #convert list to (min) heap (O(n) time ops)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #pop elements while size is bigger than k
        
    #zlogn, 1
    #adding elements is logn for heaps
    #getting minimum is 1 for heaps
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #kth largest -> n-k+1 smallest
        return self.minHeap[0] #returns the min value from heap
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)