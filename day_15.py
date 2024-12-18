import io
import time
test = 2
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
expected_b = [-1, 9021]

# Parse the input and provide as many outputs as required.
directions = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

map_grid = []
map_grid_large = []
robot_position = (0, 0)
robot_position_large = (0, 0)
move_instructions = ""

with test_data[0 if test == 1 else 1] if test else open("data") as file:
    # Process the map
    rows = 0
    for line in file:
        if not line.strip(): break
        row = []
        row_large = []
        for cols, cell in enumerate(line.strip()):
            if cell == "@":
                robot_position = (cols, rows)
                robot_position_large = (cols * 2, rows)
                row_large += ["@", "."]
            if cell == "O": row_large += ["[", "]"]
            elif cell == ".": row_large += [".", "."]
            elif cell == "#": row_large += ["#", "#"]
            row.append(cell)
        
        map_grid.append(row)
        map_grid_large.append(row_large)
        rows += 1
    
    # Process the move instructions.
    for line in file:
        move_instructions += line.strip()
        
# Do the magic here
def map_cell(cell, map_grid, value=None):
    if value: map_grid[cell[1]][cell[0]] = value
    return map_grid[cell[1]][cell[0]]

def add_cell(cell_a, cell_b):
    return (cell_a[0] + cell_b[0], cell_a[1] + cell_b[1])
    
def move(cell, instruction, map_grid, check_only=False):
    direction = directions[instruction]
    cell_type = map_cell(cell, map_grid)
    next_cell = add_cell(cell, direction)
    
    if cell_type == "#": return False
    elif cell_type == ".": return True
    elif instruction in "^v" and cell_type in "[]": # Part B needs to handle these differently.
        paired_cell = add_cell(cell, (1, 0) if cell_type == "[" else (-1, 0))
        paired_next_cell = add_cell(paired_cell, direction)
        paired_cell_type = map_cell(paired_cell, map_grid)
        
        if check_only:
            return all([
                move(next_cell, instruction, map_grid, True),
                move(paired_next_cell, instruction, map_grid, True)
            ])
        else:
            if move(cell, instruction, map_grid, True):
                move(next_cell, instruction, map_grid)
                move(paired_next_cell, instruction, map_grid)
                map_cell(next_cell, map_grid, cell_type)
                map_cell(paired_next_cell, map_grid, paired_cell_type)
                map_cell(cell, map_grid, ".")
                map_cell(paired_cell, map_grid, ".")
                return True
    else:
        if check_only:
            return move(next_cell, instruction, map_grid, True)
        else:
            if move(cell, instruction, map_grid, True):
                move(next_cell, instruction, map_grid)
                map_cell(next_cell, map_grid, cell_type)
                map_cell(cell, map_grid, ".")
                return True
    return False

def draw(map_grid, robot_position):
    boxes = []
    result = 0
    for y, row in enumerate(map_grid):
        row_string = ""
        for x, cell in enumerate(row):
            row_string += cell if (x, y) != robot_position else "@"
            if cell == "O":
                boxes += [(x, y)]
                result += (y * 100) + x
            elif cell == "[":
                boxes += [(x, y)]
                left = x
                right = len(row) - left
                top = y
                result += (y * 100) + min(left, right)
            
        print(row_string)
    print(boxes)
    return result

for instruction in move_instructions:
    direction = directions[instruction]
    next_cell = add_cell(robot_position, direction)
    moved = move(robot_position, instruction, map_grid)
    if moved:
        robot_position = next_cell

for instruction in move_instructions:
    direction = directions[instruction]
    next_cell = add_cell(robot_position_large, direction)
    moved = move(robot_position_large, instruction, map_grid_large)
    if moved:
        robot_position_large = next_cell


solve_a = draw(map_grid, robot_position)
solve_b = draw(map_grid_large, robot_position_large)

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a[0 if test == 1 else 1] else f'Fail (expected {expected_a[0 if test == 1 else 1]}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b[0 if test == 1 else 1] else f'Fail (expected {expected_b[0 if test == 1 else 1]}, got {solve_b}).'}" if test else solve_b)
