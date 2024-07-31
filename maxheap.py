import heapq
class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        heapq.heappush(self.heap, -value)
    def extract_max(self):
        if not self.heap:
            raise IndexError("Extracting from an empty heap")
        return -heapq.heappop(self.heap)
    def peek(self):
        if not self.heap:
            raise IndexError("Peeking from an empty heap")
        return -self.heap[0]
        
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)
print(max_heap.peek()) 