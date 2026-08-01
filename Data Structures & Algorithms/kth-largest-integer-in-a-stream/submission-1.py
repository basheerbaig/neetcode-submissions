class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# # Object 1 → keeps track of 3rd largest element
# obj1 = KthLargest(3, [4, 5, 8, 2])
# Initial heap = [4, 5, 8]
# add(3) → heap becomes [4, 5, 8] → kth largest = 4
# add(10) → heap becomes [5, 8, 10] → kth largest = 5


# # Object 2 → keeps track of 2nd largest element
# obj2 = KthLargest(2, [10, 7, 9])
# Initial heap = [9, 10]
# add(8) → heap stays [9, 10] → kth largest = 9
# add(11) → heap becomes [10, 11] → kth largest = 10


