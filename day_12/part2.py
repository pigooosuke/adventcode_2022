from collections import deque
import string


priorities = string.ascii_lowercase


grid = [[c for c in line]
        for line in open("input.txt").read().strip().split("\n")]
# find start/goal
x, y = [(r.index("S"), n) for n, r in enumerate(grid) if "S" in r][0]
goal_x, goal_y = [(r.index("E"), n) for n, r in enumerate(grid) if "E" in r][0]
print(f"S: {x}, {y}")
print(f"E: {goal_x}, {goal_y}")
# set a on start
grid[y][x] = "a"


def bfs(grid, pos):
    w, h = len(grid[0]), len(grid)
    q = deque([[pos]])
    seen = set([pos])
    while q:
        path = q.popleft()
        x, y = path[-1]
        if grid[y][x] == "E":
            return path
        current_priority = priorities.index(grid[y][x])
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in seen:
                if grid[y2][x2] != "E":
                    next_priority = priorities.index(grid[y2][x2])
                else:
                    next_priority = 26
                if next_priority <= current_priority + 1:
                    q.append(path + [(x2, y2)])  # queue
                    seen.add((x2, y2))


def solve():
    starts = [(c, r) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "a"]
    path = [len(bfs(grid, pos)) - 1 for pos in starts if bfs(grid, pos)]
    return min(path)


ans = solve()
print(ans)
