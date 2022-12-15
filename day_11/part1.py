import re
import operator


class Monkey(object):
    def __init__(self, id, items, operator_symbol, value, divisible, if_true, if_false):
        self.id = id
        self.items = items
        self.operator_symbol = operator_symbol
        self.value = value
        self.divisible = divisible
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_cnt = 0

    def calc(self):
        self.inspect_cnt += 1
        item = self.items.pop(0)
        operator_value = item if self.value == "old" else int(self.value)
        if self.operator_symbol == "+":
            item = operator.add(item, operator_value)
        elif self.operator_symbol == "*":
            item = operator.mul(item, operator_value)
        item = item // 3
        if item % self.divisible == 0:
            return item, self.if_true
        else:
            return item, self.if_false

    def catch_item(self, item):
        self.items.append(item)


monkeys = []
with open("input.txt", "r") as f:
    blocks = f.read().strip().split("\n\n")
    for block in blocks:
        lines = block.split("\n")
        m = re.search(r'\d+', lines[0])
        monkey_id = int(m.group(0))
        items = list(map(int, lines[1].split(":")[1].strip().split(", ")))
        operator_symbol, value = lines[2].split("old ")[1].split(" ")
        m = re.search(r'\d+', lines[3])
        divisible = int(m.group(0))
        m = re.search(r'\d+', lines[4])
        if_true = int(m.group(0))
        m = re.search(r'\d+', lines[5])
        if_false = int(m.group(0))
        monkeys.append(
            Monkey(id, items, operator_symbol, value, divisible, if_true, if_false)
        )


def solve():
    for _ in range(20):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            while len(monkey.items) > 0:
                item, pass_id = monkey.calc()
                monkeys[pass_id].catch_item(item)
    print([m.items for m in monkeys])
    print([m.inspect_cnt for m in monkeys])
    top_two_cnt = sorted([m.inspect_cnt for m in monkeys], reverse=True)[:2]
    ans = top_two_cnt[0] * top_two_cnt[1]
    return ans


ans = solve()
print(ans)
