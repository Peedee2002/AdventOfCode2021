from __future__ import annotations
from dataclasses import dataclass
import heapq
# djikstra's
@dataclass
class Node:
    value: int
    index: tuple[int, int]
    distance: float = float('inf')
    previous: Node = None

    def __lt__(self, other: Node):
        return self.distance < other.distance

def get_neighbours(grid: list[list[Node]], x: int, y: int):
    return (grid[i][j] for i, j in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)] if 0 <= i < len(grid) and 0 <= j < len(grid))

def next_tile(grid):
    return [[1 + (value) % 9 for value in row] for row in grid]

# these 2 functions are crass
def expand_rows(grid):
    new_grid = []
    for row in grid:
        new_row = row.copy()
        for i in range(4):
            new_row += [1 + (value + i) % 9 for value in row]
        new_grid.append(new_row)
    return new_grid

def expand_grid(grid):
    grid2 = next_tile(grid)
    grid3 = next_tile(grid2)
    grid4 = next_tile(grid3)
    grid5 = next_tile(grid4)
    return expand_rows(grid) + expand_rows(grid2) + expand_rows(grid3) + expand_rows(grid4) + expand_rows(grid5)
    

if __name__ == '__main__':
    grid = [[int(num) for num in line[:-1]] for line in open('input.in')]
    grid = expand_grid(grid)
    grid = [[Node(value, (x, y)) for y, value in enumerate(row)] for x, row in enumerate(grid)]
    grid[0][0].distance = 0
    queue: list[Node] = []
    heapq.heappush(queue, grid[0][0])
    while len(queue) != 0:
        curr = heapq.heappop(queue)
        if curr.index == (len(grid) - 1, len(grid) - 1):
            print(curr.distance)
            exit()
        for neighbour in get_neighbours(grid, curr.index[0], curr.index[1]):
            alt = curr.distance + neighbour.value
            if alt < neighbour.distance:
                neighbour.distance = alt
                neighbour.previous = curr
                if neighbour not in queue:
                    heapq.heappush(queue, neighbour)
