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
    head_state = [0, 0]
    tail_state = [0, 0]
    ans = set()
    ans.add(tuple(tail_state))
    for move in moves:
        direction, step = move
        for _ in range(step):
            # head move
            if direction == "D":
                head_state[1] -= 1
            elif direction == "U":
                head_state[1] += 1
            elif direction == "L":
                head_state[0] -= 1
            elif direction == "R":
                head_state[0] += 1
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
                ans.add(tuple(tail_state))
                continue
            # slide
            if direction == "D":
                tail_state[1] -= 1
            elif direction == "U":
                tail_state[1] += 1
            elif direction == "L":
                tail_state[0] -= 1
            elif direction == "R":
                tail_state[0] += 1
            ans.add(tuple(tail_state))
    return len(ans)


ans = solve()
print(ans)
