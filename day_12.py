test = 0
file = 'test'if test else 'data'

solve_a = 0
solve_b = 0
expected_a = 1930
expected_b = 1206

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
    plant = map_grid[y][x][0]
    size = 0
    fences = 0
    plots = []
    min_x, min_y, max_x, max_y = 0,0,0,0

    # Part A - Define the region and count how many "fences" it has.
    to_visit = [(x, y)]
    
    while to_visit:
        current_cell = to_visit.pop()
        plots.append(current_cell)

        min_x, max_x = min(min_x, current_cell[0]), max(max_x, current_cell[0])
        min_y, max_y = min(min_y, current_cell[1]), max(max_y, current_cell[1])
        
        # If we've visited this cell before, don't bother checking it's neighbors.
        if map_grid[current_cell[1]][current_cell[0]][1]: continue
        
        for neighbor in directions:
            check_cell = (current_cell[0] + neighbor[0], current_cell[1] + neighbor[1])
            
            
            # Is it out of bounds / at the border)?
            if not (0 <= check_cell[0] < bounds[0] and 0 <= check_cell[1] < bounds[1]):
                fences += 1
                continue
            
            # Is it a different type (not part of our plot)?
            if map_grid[check_cell[1]][check_cell[0]][0] != plant:
                fences += 1
                continue
            
            # Have we visited this cell before?
            if map_grid[check_cell[1]][check_cell[0]][1]:
                continue
            
            to_visit.append(check_cell)
        map_grid[current_cell[1]][current_cell[0]] = (plant, True)
        size += 1

    sides = scan_sides(plots, (min_x, min_y), (max_x - min_x + 1, max_y - min_y + 1))

    region = {
        'size': size,
        'fences': fences,
        'sides': sides
    }
    
    return region

# This code is ugly, but it works.
def scan_sides(plots, offset, bounds):
    # Re-create the local region
    region_grid = [[True if (x + offset[0], y + offset[1]) in plots else False for x in range(bounds[0])]  for y in range(bounds[1])]
    
    sides = 0

    # Scan top edges
    for y in range(bounds[1]):
        edge_flag = False
        for x in range(bounds[0]):
            check_edge_flag = (region_grid[y][x] and y == 0) or (region_grid[y][x] and not region_grid[y - 1][x])
            if check_edge_flag and not edge_flag:
                sides += 1
            edge_flag = check_edge_flag

    # Scan left edges
    for x in range(bounds[0]):
        edge_flag = False
        for y in range(bounds[1]):
            check_edge_flag = (region_grid[y][x] and x == 0) or (region_grid[y][x] and not region_grid[y][x - 1])
            if check_edge_flag and not edge_flag:
                sides += 1
            edge_flag = check_edge_flag
    
    # Scan bottom edges
    for y in range(bounds[1]):
        edge_flag = False
        for x in range(bounds[0]):
            check_edge_flag = (region_grid[y][x] and y == bounds[1] - 1) or (region_grid[y][x] and not region_grid[y + 1][x])
            if check_edge_flag and not edge_flag:
                sides += 1
            edge_flag = check_edge_flag
    
    # Scan right edges
    for x in range(bounds[0]):
        edge_flag = False
        for y in range(bounds[1]):
            check_edge_flag = (region_grid[y][x] and x == bounds[0] - 1) or (region_grid[y][x] and not region_grid[y][x + 1])
            if check_edge_flag and not edge_flag:
                sides += 1
            edge_flag = check_edge_flag
    
    return sides



regions = []

# Traverse the map grid, flood filling regions as you go.
for y, row in enumerate(map_grid):
    for x, cell in enumerate(row):
        # If we've visited this cell before, skip it.
        if cell[1]: continue
        regions.append(flood_fill(x, y, map_grid))

solve_a = sum([region['size'] * region['fences'] for region in regions])
solve_b = sum([region['size'] * region['sides'] for region in regions])

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)