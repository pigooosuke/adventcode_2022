import numpy as np


grid = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        grid.append(list(map(int, list(line))))
grid = np.array(grid)
print(grid)
print(grid.shape)


def count_trees(my_val, vals):
    cnt = 0
    for v in vals:
        cnt += 1
        if v >= my_val:
            break
    return cnt


def solve():
    ans = np.zeros(grid.shape[0] * grid.shape[1], dtype=int).reshape(grid.shape)
    n_row = grid.shape[0]
    n_col = grid.shape[1]
    for i in range(n_row):
        for j in range(n_col):
            if i == 0 or i == n_row - 1 or j == 0 or j == n_col - 1:
                ans[i, j] = 0
                continue
            # up
            up_trees = grid[:i, j]
            up_trees = up_trees[::-1]
            # down
            down_trees = grid[(i + 1):, j]
            # left
            left_trees = grid[i, :j]
            left_trees = left_trees[::-1]
            # right
            right_trees = grid[i, (j + 1):]
            # score
            score = count_trees(grid[i, j], up_trees) * count_trees(grid[i, j], down_trees) * count_trees(grid[i, j], left_trees) * count_trees(grid[i, j], right_trees)
            ans[i, j] = score
    return ans.max()


ans = solve()
print(ans)
