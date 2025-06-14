"""
Q1046
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                diff = first - second
                heapq.heappush(stones, -diff)
        return -stones[0] if stones else 0


if __name__ == "__main__":
    sol = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    print(sol.lastStoneWeight(stones))

"""
Time Complexity:
heapify: O(n)
pop and push: 3.O(log(n))
while loop: O(n)
Overall time complexity: O(n.log(n)), where n is the number of elements in the heap
"""


