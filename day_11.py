test = 0
file = 'test'if test else 'data'

solve_a = 0
solve_b = 0

expected_a = 55312
expected_b = 0

stones = []
stone_id = {}

with open(file) as f:
    line = f.readline().strip()
    stones = {}
    for stone in line.split(" "):
        stones[int(stone)] = 1

def run_rules(stone):
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
    new_stones = {}
    for stone_value, stone_count in stones.items():
        blinked_stones = run_rules(stone_value)
        for blinked_stone in blinked_stones:
            if blinked_stone not in new_stones.keys(): new_stones[blinked_stone] = 0
            new_stones[blinked_stone] += stone_count
    
    return new_stones

stones_a = stones
for blink_number in range(25):
    new_stones = blink(stones_a)
    stones_a = new_stones
    
stones_b = stones
for blink_number in range(75):
    new_stones = blink(stones_b)
    stones_b = new_stones

solve_a = sum([stone_count for stone_count in stones_a.values()])
solve_b = sum([stone_count for stone_count in stones_b.values()])

print(solve_a)
print(solve_b)
