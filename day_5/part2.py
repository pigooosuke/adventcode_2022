def read_input():
    with open("input.txt", "r") as f:
        init_space, moves = f.read().split("\n\n")
        lines = [line for line in init_space.split("\n")]
        size = len(lines[-1].split())
        # init state
        boxes = [[] for i in range(size)]
        for line in lines[::-1][1:]:
            line = line.rstrip()
            for i, char in enumerate(line):
                p, q = divmod(i, 4)
                if q == 1 and char != " ":
                    boxes[p].append(char)
        # actions
        actions = []
        for move in moves.strip().split("\n"):
            tokens = move.split(" ")
            actions.append(tuple(map(int, (tokens[1], tokens[3], tokens[5]))))

    return boxes, actions


def solve():
    boxes, actions = read_input()
    for action in actions:
        tokens = boxes[action[1] - 1][-action[0]:]
        boxes[action[2] - 1].extend(tokens)
        for _ in range(action[0]):
            boxes[action[1] - 1].pop()

    return "".join([box[-1] for box in boxes])


ans = solve()
print(ans)
