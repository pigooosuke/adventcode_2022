import string


priorities = dict()
for priority, char in enumerate(string.ascii_letters, start=1):
    priorities[char] = priority


def solve():
    ans = 0
    with open("input.txt", "r") as f:
        for line in f:
            keep = set()
            chars = line.strip()
            size = len(chars)
            for i, char in enumerate(chars, start=1):
                if i <= size / 2:
                    keep.add(char)
                    continue
                if char in keep:
                    ans += priorities[char]
                    break
    return ans


ans = solve()
print(ans)
