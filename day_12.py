test = 0
file = 'test'if test else 'data'

solve_a = 0
solve_b = 0
expected_a = 1930
expected_b = 0

map_grid = []
directions = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1)
    ]
bounds = (0, 0)

with open(file) as f:
    line = f.readline().strip()
    cols = len(line)
    rows = 0
    
    while line:
        # Record each cell as it's 'plant' value, and a boolean 'visited' value.
        row = [(plant, False) for plant in line]
        map_grid.append(row)
        rows += 1
        line = f.readline().strip()
        
    bounds = (cols, rows)

def flood_fill(x, y, map_grid):
    target = map_grid[y][x][0]
    size = 0
    fences = 0
    to_visit = [(x, y)]
    
    while to_visit:
        current_cell = to_visit.pop()
        
        # If we've visited this cell before, don't bother checking it's neighbors.
        if map_grid[current_cell[1]][current_cell[0]][1]: continue
        
        for neighbor in directions:
            check_cell = (current_cell[0] + neighbor[0], current_cell[1] + neighbor[1])
            
            
            # Is it out of bounds (at the border)?
            if not (0 <= check_cell[0] < bounds[0] and 0 <= check_cell[1] < bounds[1]):
                fences += 1
                continue
            
            # Is it a different type (not part of our plot)?
            if map_grid[check_cell[1]][check_cell[0]][0] != target:
                fences += 1
                continue
            
            # Have we visited this cell before?
            if map_grid[check_cell[1]][check_cell[0]][1]:
                continue
            
            to_visit.append(check_cell)
        map_grid[current_cell[1]][current_cell[0]] = (target, True)
        size += 1
    
    return (size, fences)

regions = []

# Traverse the map grid, flood filling regions as you go.
for y, row in enumerate(map_grid):
    for x, cell in enumerate(row):
        # If we've visited this cell before, skip it.
        if cell[1]: continue
        regions.append(flood_fill(x, y, map_grid))

solve_a = sum([region[0] * region[1] for region in regions])

print(solve_a)
print(solve_b)
