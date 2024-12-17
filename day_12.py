test = 0
file = 'test'if test else 'data'

solve_a = 0
solve_b = 0
expected_a = 1930
expected_b = 1206

map_grid = []

# List of directions in clockwise order. Using a direction as a key gives the next direction.
directions = {
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0)
    }

bounds = (0, 0)

with open(file) as f:
    for line in f:
        # Record each cell as it's 'plant' value, and a boolean 'visited' value.
        map_grid.append([(plant, False) for plant in line.strip()])
        
    bounds = (len(map_grid[0]), len(map_grid))

def in_bounds(pos, bounds):
    if (0 <= pos[0] < bounds[0] and 0 <= pos[1] < bounds[1]): return True
    return False

def map_cell(cell, value=None):
    global map_grid
    if value: map_grid[cell[1]][cell[0]] = value
    
    return map_grid[cell[1]][cell[0]]

# BFS to define the regions.
def flood_fill(x, y, map_grid):
    plant = map_cell((x,y))[0]
    plots = {}

    to_visit = [(x, y)]
    
    while to_visit:
        current_cell = to_visit.pop()
        current_cell_fences = []
        
        for neighbor in directions:
            check_cell = (current_cell[0] + neighbor[0], current_cell[1] + neighbor[1])
            
            # Is it out of bounds or a different type (not part of our plot)?
            # If so, add a fence and move on.
            if not in_bounds(check_cell, bounds) or map_cell(check_cell)[0] != plant:
                current_cell_fences.append(neighbor)
                continue
            
            # If we haven't visited the checked cell before, make sure we visit it.
            if not map_cell(check_cell)[1] and check_cell not in to_visit:
                to_visit.append(check_cell)
            
        plots[current_cell] = current_cell_fences
        
        # Mark this cell as visited.
        map_cell(current_cell, (plant, True))
    
    # Count the number of corners / sides in this region.
    # A corner can be discovered by checking if a plot's fence is not continued in the next cell
    sides = 0
    for plot, fences in plots.items():
        for fence in fences:
            neighbor = directions[fence]
            neighbor_plot = (plot[0] + neighbor[0], plot[1] + neighbor[1])
            if neighbor_plot not in plots or fence not in plots[neighbor_plot]: sides += 1
    
    size = len(plots)
    fences = sum([len(fences) for fences in plots.values()])
    
    return (size * fences, size * sides)

# Traverse the map grid, flood filling regions as you go.
for y, row in enumerate(map_grid):
    for x, cell in enumerate(row):
        # If we've visited this cell before, skip it.
        if cell[1]: continue
    
        result = flood_fill(x, y, map_grid)
        solve_a += result[0]
        solve_b += result[1]

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)
