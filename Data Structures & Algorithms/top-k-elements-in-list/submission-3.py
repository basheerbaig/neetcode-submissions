from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []

        # build [count, value] pairs
        for val, cnt in count.items():
            res.append([cnt, val])

        # sort ascending by count
        res.sort()

        res1 = []
        # iterate from end (largest freq to smallest)
        for i in range(len(res) - 1, -1, -1):
            if len(res1) < k:
                res1.append(res[i][1])
            else:
                break

        return res1
