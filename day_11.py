test = 0
file = 'test'if test else 'data'

solve_a = 0
solve_b = 0

expected_a = 55312
expected_b = 0

stones = []

with open(file) as f:
    line = f.readline().strip()
    stones = [int(stone)for stone in line.split(" ")]

def run_rules(index, stone_row):
    stone = stone_row[index]
    if stone == 0:
        stone = 1
        return [stone]
    elif not len(str(stone)) % 2:
        stone_str = str(stone)
        new_stone = int(stone_str[len(stone_str) // 2:])
        stone = int(stone_str[:(len(stone_str) // 2)])
        return [stone, new_stone]
    else:
        return [stone * 2024]

def blink(stones):
    new_stones = []
    for index in range(len(stones)):
        new_stones += run_rules(index, stones)
    
    return new_stones

for blink_number in range(75):
    new_stones = blink(stones)
    stones = new_stones

solve_a = len(stones)

print(solve_a, f"(test {expected_a})")
print(solve_b, f"(test {expected_b})")
