import io
from enum import Enum
test = 0
test_data = []
test_data.append(io.StringIO(
"""
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""
))
test_data[0].readline() # Get rid of the first empty line (it's only there for display purposes).
test_data.append(io.StringIO(
"""
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
))
test_data[1].readline() # Get rid of the first empty line (it's only there for display purposes).

solve_a = 0
solve_b = 0
expected_a = [2028, 10092]
expected_b = [-1, -1]

# Parse the input and provide as many outputs as required.
directions = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

map_grid = []
robot_position = (0, 0)
move_instructions = ""

with test_data[0 if test == 1 else 1] if test else open("data") as file:
    # Process the map
    rows = 0
    for line in file:
        if not line.strip(): break
        row = []
        for cols, cell in enumerate(line.strip()):
            if cell == "@":
                robot_position = (cols, rows)
                cell = "."
            row.append(cell)
        
        map_grid.append(row)
        rows += 1
    
    # Process the move instructions.
    for line in file:
        move_instructions += line.strip()
# Do the magic here

print(move_instructions)

def move(cell, direction, map_grid):
    cell_type = map_grid[cell[1]][cell[0]]
    next_cell = (cell[0] + direction[0], cell[1] + direction[1])
    if map_grid[next_cell[1]][next_cell[0]] == "#": return False
    if map_grid[next_cell[1]][next_cell[0]] == "O":
        can_move = move(next_cell, direction, map_grid)
        predicted_cell = next_cell if can_move else cell
        map_grid[predicted_cell[1]][predicted_cell[0]] = cell_type
        return can_move
    else:
        map_grid[cell[1]][cell[0]] = "."
        map_grid[next_cell[1]][next_cell[0]] = cell_type
        return True

for instruction in move_instructions:
    direction = directions[instruction]
    can_move = move(robot_position, direction, map_grid)
    robot_position = (robot_position[0] + direction[0], robot_position[1] + direction[1]) if can_move else robot_position
    
for y, row in enumerate(map_grid):
    row_string = ""
    for x, cell in enumerate(row):
        row_string += cell if (x, y) != robot_position else "@"
        if cell == "O":
            solve_a += (y * 100) + x
    print(row_string)

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a[0 if test == 1 else 1] else f'Fail (expected {expected_a[0 if test == 1 else 1]}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b[0 if test == 1 else 1] else f'Fail (expected {expected_b[0 if test == 1 else 1]}, got {solve_b}).'}" if test else solve_b)
