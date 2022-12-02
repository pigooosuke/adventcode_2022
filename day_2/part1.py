# A/X: Rock
# B/Y: Paper
# C/Z: Scissors

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
    if me == "X":
        score += 1
        if opp == "A":
            score += 3
        elif opp == "B":
            score += 0
        elif opp == "C":
            score += 6
    elif me == "Y":
        score += 2
        if opp == "A":
            score += 6
        elif opp == "B":
            score += 3
        elif opp == "C":
            score += 0
    elif me == "Z":
        score += 3
        if opp == "A":
            score += 0
        elif opp == "B":
            score += 6
        elif opp == "C":
            score += 3
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
