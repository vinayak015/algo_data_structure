"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
"""

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols

        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)
        state = (0, 0, k) # row, col, quotas
        queue = deque([(*state, 0)])
        seen = set(state)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, k, steps = queue.popleft()
            if (row, col) == target:
                return steps
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if is_valid(next_row, next_col):
                    if grid[next_row][next_col] == 0:
                        if (next_row, next_col, k) not in seen:
                            visited_state = (next_row, next_col, k)
                            seen.add(visited_state)
                            queue.append((*visited_state, steps+1))
                    elif k and (next_row, next_col, k-1) not in seen:
                        visited_state = (next_row, next_col, k-1)
                        seen.add(visited_state)
                        queue.append((*visited_state, steps+1))
        return -1


