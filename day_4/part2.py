
def solve():
    ans = 0
    with open("input.txt", "r") as f:
        for line in f:
            first, second = line.strip().split(",")
            first_start, first_end = map(int, first.split("-"))
            second_start, second_end = map(int, second.split("-"))
            first_set, second_set = set(), set()
            for i in range(first_start, first_end + 1):
                first_set.add(i)
            for i in range(second_start, second_end + 1):
                second_set.add(i)
            if len(first_set & second_set) > 0:
                ans += 1

    return ans


ans = solve()
print(ans)
