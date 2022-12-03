import string


priorities = dict()
for priority, char in enumerate(string.ascii_letters, start=1):
    priorities[char] = priority


def solve():
    ans = 0
    keep = [set() for i in range(3)]
    with open("input.txt", "r") as f:
        for index, line in enumerate(f, start=1):
            chars = line.strip()
            for char in chars:
                keep[index % 3].add(char)
            if index % 3 == 0 and index != 0:
                badge = keep[0] & keep[1] & keep[2]
                ans += priorities[badge.pop()]
                keep = [set() for i in range(3)]

    return ans


ans = solve()
print(ans)
