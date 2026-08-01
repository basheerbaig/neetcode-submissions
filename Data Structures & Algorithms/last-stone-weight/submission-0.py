import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to a max-heap by negating values
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)  # heaviest stone
            y = -heapq.heappop(stones)  # second heaviest stone

            if x != y:
                heapq.heappush(stones, -(x - y))  # push the difference back

        return -stones[0] if stones else 0
