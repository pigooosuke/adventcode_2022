# A: Rock
# B: Paper
# C: Scissors

# X: lose
# Y: draw
# Z: win

# select score
# Rock: 1
# Paper: 2
# Scissors: 3

# round score
# win: 6
# draw: 3
# lose: 0


def evaluation(opp, me):
    score = 0
    # lose
    if me == "X":
        score += 0
        if opp == "A":
            score += 3
        elif opp == "B":
            score += 1
        elif opp == "C":
            score += 2
    elif me == "Y":
        score += 3
        if opp == "A":
            score += 1
        elif opp == "B":
            score += 2
        elif opp == "C":
            score += 3
    elif me == "Z":
        score += 6
        if opp == "A":
            score += 2
        elif opp == "B":
            score += 3
        elif opp == "C":
            score += 1
    return score


def solve():
    ans = 0
    with open("input.txt", "r") as f:
        for line in f:
            value = line.strip()
            opp, me = value.split(" ")
            score = evaluation(opp, me)
            ans += score
    return ans


ans = solve()
print(ans)
