test = 0
file = 'test' if test else 'data'

solve_a = 0
solve_b = 0

directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]

map_obstacles = []
bounds = (0,0)

guard_facing = directions[0]
guard_position = (0, 0)
guard_start_position = (0, 0)

with open(file) as f:
    line = f.readline().strip()
    
    cols = len(line)
    rows = 0
    
    while line:
        for index, cell in enumerate(line):
            if cell == "#": map_obstacles.append((index, rows))
            elif cell == "^": guard_position, guard_start_position = (index, rows), (index, rows)
            
        rows += 1
        line = f.readline().strip()
    
    bounds = (cols, rows)

def in_bounds(position, bounds):
    global bounds
    return 0 <= position[0] < bounds[0] and 0 <= position[1] < bounds[1]

# Follow the guard's path (and determine if it loops)
def traverse_map(position, facing, obstacles):
    map_grid = {}
    
    while in_bounds(position):
        # Mark the guard's current position
        map_grid[position] = map_grid[position] + [facing] if position in map_grid.keys() else [facing]

        # Grab the next cell for checking
        next_cell = (position[0] + facing[0], position[1] + facing[1])

        # Check if the guard is moving out of bounds (no loop)
        if not (in_bounds(next_cell)): break
        
        # Check if the guard is in a loop
        if next_cell in map_grid and facing in map_grid[next_cell]:
            return (map_grid, True)
        
        # Check if the guard will hit an obstacle
        if next_cell in obstacles:
            facing = directions[(directions.index(facing) + 1) % len(directions)]
        else:
            position = next_cell
    
    return (map_grid, False)

initial_run = traverse_map(guard_start_position, guard_facing, map_obstacles)

solve_a = len(initial_run[0])

for marked_position in set(initial_run[0].keys()):
    if marked_position == guard_start_position: continue
    solve_b += 1 if traverse_map(guard_start_position, guard_facing, map_obstacles + [marked_position])[1] else 0

print(solve_a)
print(solve_b)
