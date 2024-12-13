test = 1
file = 'test'if test else 'data'

solve_a = 0
solve_b = 0

expected_a = 55312
expected_b = 0

stones = []

with open(file) as f:
    line = f.readline().strip()
    stones = [int(stone)for stone in line.split(" ")]

def run_rules(stone, index, stone_row):
    if stone == 0:
        stone_row[index] = 1
        return [stone]
    elif stone > 9 and not stone % 2:
        stone_str = str(stone)
        new_stone = stone_str[(stone_str) // )]
        pass

print(stones)
print(solve_a, f"(expected {expected_a})")
print(solve_b, f"(expected {expected_b})")
