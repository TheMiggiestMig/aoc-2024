import io
import re
import math

test = 0
test_data = io.StringIO(
"""
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
)
test_data.readline() # Get rid of the first empty line (it's only there for display purposes).

solve_a = 0
solve_b = 0
expected_a = 12
expected_b = "No test part B"

# Parse the input and provide as many outputs as required.
robots = []
with test_data if test else open("data") as file:
    for line in file:
        px, py, vx, vy = [int(n) for n in re.findall(r"-?\d+", line)]
        robots.append(((px, py), (vx, vy)))

map_bounds = (11, 7) if test else (101, 103)
ticks = 100

# Do the magic here
def move(position, velocity):
    new_x = (position[0] + velocity[0] * ticks) % map_bounds[0]
    new_y = (position[1] + velocity[1] * ticks) % map_bounds[1]

    return (new_x, new_y)

# Move the robots around
updated_robots = {}
for robot in robots:
    cell = move(*robot)
    updated_robots[cell] = updated_robots.setdefault(cell, 0) + 1

quadrants = [0, 0, 0, 0]
# Calculate how many robots per quadrant.
for y in range(map_bounds[1]):
    row = ""
    if y == map_bounds[1] // 2:
        continue
    for x in range(map_bounds[0]):
        if x == map_bounds[0] // 2:
            continue
        if (x, y) in updated_robots:
            quadrants[(0 if y < map_bounds[1] // 2 else 2) + (0 if x < map_bounds[0] // 2 else 1)] += updated_robots[(x, y)]

solve_a = math.prod(quadrants)

ticks = 0
largest_mirror_count = 0
half_map = map_bounds[0] // 2
while ticks < 10000:
    ticks += 1
    # Part B
    # Calculate how many robots per quadrant.
    updated_robots = {}
    for robot in robots:
        cell = move(*robot)
        updated_robots[cell] = updated_robots.setdefault(cell, 0) + 1
    
    # Check if there are mirrored robots.
    mirror_count = 0
    for robot in updated_robots:
        if robot == (map_bounds[0] // 2, map_bounds[1] // 2): continue
        dx = half_map - robot[0]
        if (half_map - dx, robot[1]) in updated_robots: mirror_count += 1
    
    largest_mirror_count = max(largest_mirror_count, mirror_count)
    if mirror_count < 500:
        continue

    image = ""
    for y in range(map_bounds[1]):
        row = ""
        for x in range(map_bounds[0]):
            if (x, y) in updated_robots:
                row += str(updated_robots[(x, y)])
            else:
                row += "."
        image += row + "\n"
    
    print(image)
    solve_b = ticks
    break

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)