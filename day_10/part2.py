def solve():
    values = [1]
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip().split(' ')
            values.append(values[-1])
            if line[0] == 'addx':
                values.append(int(line[1]) + values[-1])
    for i in range(len(values)):
        print('#' if abs(values[i] - (i % 40)) <= 1 else ' ', end='')
        print('\n' if ((i + 1) % 40 == 0) else '', end='')


ans = solve()
print(ans)
