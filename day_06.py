# Not yet solved part B
test = 0
file = 'test' if test else 'data'

import time

solve_a = 0
solve_b = 0
debug_step = 0
debug_total_steps = 55 if test else 6373

directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]

map_grid = []
obstacles = []
bounds = (0,0)

guard_facing = directions[0]
guard_position = (0, 0)

with open(file) as f:
    line = f.readline().strip()
    
    cols = len(line)
    rows = 0
    
    while line:
        for index, cell in enumerate(line):
            if cell == "#": obstacles.append((index, rows))
            elif cell == "^": guard_position = (index, rows)
            
        rows += 1
        map_grid.append([0] * cols)
        line = f.readline().strip()
    
    bounds = (cols, rows)
    
# DEBUG - Since I'm doing this on online-python.com, it keeps timing out.
# This lets me set the state and resume the search.
#
# Note: This will give an invalid solve_a value, since we don't restore the map_grid.
# Copied from my debug console output.
guard_position, guard_facing, solve_b, debug_step = (76, 128), (-1, 0), 2405, 6331

# Map the guard's path while they're still on the map.
while 0 <= guard_position[0] < bounds[0] and 0 <= guard_position[1] < bounds[1]:
    debug_step += 1
    next_cell = (guard_position[0] + guard_facing[0], guard_position[1] + guard_facing[1])
    
    # Check if the guard is moving out of bounds
    if not (0 <= next_cell[0] < bounds[0] and 0 <= next_cell[1] < bounds[1]): break
    
    # Check if they hit an obstacle
    if next_cell in obstacles:
        guard_facing = directions[(directions.index(guard_facing) + 1) % len(directions)]
    else:
        # For Solve B - Simulate an obstacle being right in front.
        temp_obstacles = obstacles + [next_cell]
        temp_guard_position = (guard_position[0], guard_position[1])
        temp_guard_facing = (guard_facing[0], guard_facing[1])
        temp_map_grid = [[list() for x in range(bounds[0])] for y in range(bounds[1])]
        
        while 0 <= temp_guard_position[0] < bounds[0] and 0 <= temp_guard_position[1] < bounds[1]:
            temp_next_cell = (temp_guard_position[0] + temp_guard_facing[0], temp_guard_position[1] + temp_guard_facing[1])
            
            # Check if the guard is moving out of bounds
            if not (0 <= temp_next_cell[0] < bounds[0] and 0 <= temp_next_cell[1] < bounds[1]): break
            
            if temp_guard_facing in temp_map_grid[temp_next_cell[1]][temp_next_cell[0]]:
                # We found a loop!
                print(f"[DEBUG] Found {solve_b + 1} loops! [@ step {debug_step}/{debug_total_steps} ({(debug_step/debug_total_steps)*100:0.2f}%)]; guard_position, guard_facing, solve_b, debug_step = {guard_position}, {guard_facing}, {solve_b}, {debug_step-1}")
                solve_b += 1
                time.sleep(0.000001)
                break
            
            if temp_next_cell in temp_obstacles:
                temp_guard_facing = directions[(directions.index(temp_guard_facing) + 1) % len(directions)]
            else:
                temp_map_grid[temp_guard_position[1]][temp_guard_position[0]].append(temp_guard_facing)
                temp_guard_position = temp_next_cell
        
        del temp_obstacles
        del temp_map_grid
        
        map_grid[guard_position[1]][guard_position[0]] += 1
        guard_position = next_cell

solve_a = sum([1 for row in map_grid for col in row if col > 0])

print(solve_a)
print(solve_b)
