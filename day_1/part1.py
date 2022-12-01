def solve():
    ans = 0
    keep = 0
    with open("input.txt", "r") as f:
        for line in f:
            value = line.strip()
            if len(value) == 0:
                ans = max(ans, keep)
                keep = 0
            else:
                keep += int(value)
    return ans


ans = solve()
print(ans)
