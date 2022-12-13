import numpy as np


grid = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        grid.append(list(map(int, list(line))))
grid = np.array(grid)
print(grid)
print(grid.shape)


def solve():
    ans = np.zeros(grid.shape[0] * grid.shape[1], dtype=bool).reshape(grid.shape)
    n_row = grid.shape[0]
    n_col = grid.shape[1]
    for i in range(n_row):
        for j in range(n_col):
            if i == 0 or i == n_row - 1 or j == 0 or j == n_col - 1:
                ans[i, j] = True
                continue
            if min(
                max(grid[:i, j]),
                max(grid[(i + 1):, j]),
                max(grid[i, :j]),
                max(grid[i, (j + 1):])
            ) < grid[i, j]:
                ans[i, j] = True
    print(ans)
    return ans.sum()


ans = solve()
print(ans)
