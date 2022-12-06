
def solve():
    with open("input.txt", "r") as f:
        chars = f.read().strip()
        size = len(chars)
        for i in range(size):
            if len(set(chars[i:i + 4])) == 4:
                return i + 4


ans = solve()
print(ans)
