def solve():
    ans = []
    keep = 0
    with open("input.txt", "r") as f:
        for line in f:
            value = line.strip()
            if len(value) == 0:
                ans.append(keep)
                keep = 0
            else:
                keep += int(value)
    ans.sort(reverse=True)
    return sum(ans[:3])


ans = solve()
print(ans)
