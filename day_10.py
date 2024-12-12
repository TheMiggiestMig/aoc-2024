test = 1
file = 'test' if test else 'data'

solve_a = 0
solve_b = 0

map_grid = []
bounds = (0, 0)

directions = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1)
]

# Parse the file
with open(file) as f:
    line = f.readline().strip()
    bounds_x = len(line)
    bounds_y = 0

    while line:
        map_grid.append([int(cell) for cell in line])

        bounds_y += 1
        line = f.readline().strip()

bounds = (bounds_x, bounds_y)

def traverse_all_paths(x:int, y:int, height=0):
    score = 0
    if height == 9: return 1

    for direction in directions:
        next_cell = (x + direction[0], y + direction[1])
        if 0 <= next_cell[0] < bounds[0] and 0 <= next_cell[1] < bounds[1] and map_grid[next_cell[1]][next_cell[0]] == height + 1:
            score += traverse_all_paths(*next_cell, height + 1)
    
    return score

for y, row in enumerate(map_grid):
    for x, height in enumerate(row):
        solve_a += traverse_all_paths(x, y, height)

print(solve_a)