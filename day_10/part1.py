def solve():
    values = [1]
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip().split(' ')
            values.append(values[-1])
            if line[0] == 'addx':
                values.append(int(line[1]) + values[-1])
    return sum([x * values[x - 1] for x in range(20, 221, 40)])


ans = solve()
print(ans)
