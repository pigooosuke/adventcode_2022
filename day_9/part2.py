moves = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction, step = line.split(" ")
        moves.append((direction, int(step)))
print(f"total steps: {len(moves)}")


def sign(v):
    if v > 0:
        return 1
    elif v < 0:
        return -1
    raise ValueError("unexpected")


def solve():
    states = [[0, 0] for _ in range(10)]
    ans = set()
    ans.add(tuple(states[-1]))
    for move in moves:
        direction, step = move
        for _ in range(step):
            # head move
            if direction == "D":
                states[0][1] -= 1
            elif direction == "U":
                states[0][1] += 1
            elif direction == "L":
                states[0][0] -= 1
            elif direction == "R":
                states[0][0] += 1
            for i in range(len(states) - 1):
                head_state = states[i]
                tail_state = states[i + 1]
                # tail follow
                diff = (head_state[0] - tail_state[0], head_state[1] - tail_state[1])
                # stay
                if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
                    continue
                # diag
                if diff[0] != 0 and diff[1] != 0:
                    follow_x = sign(diff[0])
                    follow_y = sign(diff[1])
                    tail_state[0] += follow_x
                    tail_state[1] += follow_y
                    if i == len(states) - 2:
                        ans.add(tuple(tail_state))
                    continue
                # slide
                if diff[0] == -2:
                    tail_state[0] -= 1
                elif diff[0] == 2:
                    tail_state[0] += 1
                elif diff[1] == -2:
                    tail_state[1] -= 1
                elif diff[1] == 2:
                    tail_state[1] += 1
                if i == len(states) - 2:
                    ans.add(tuple(tail_state))
    return len(ans)


ans = solve()
print(ans)
