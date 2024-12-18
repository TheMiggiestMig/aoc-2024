import io
import heapq

test = 1
test_data = []
test_data.append(io.StringIO(
"""
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
))
test_data[-1].readline()
test_data.append(io.StringIO(
"""
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
))
test_data[-1].readline()

solve_a = 0
solve_b = 0
expected_a = [7036, 11048]
expected_b = [45, 64]

# Parse the input and provide as many outputs as required.
step_cost = 1
turn_cost = 1000
directions = {
    (1,0): [(0, -1), (0, 1)],
    (0, -1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, 1), (0, -1)],
    (0, 1): [(-1, 0), (1, 0)]
}
start_position, end_position = (0, 0), (0, 0)
map_grid = []
bounds = (0, 0)

with test_data[test - 1] if test else open("data") as file:
    rows = 0
    for line in file:
        row = [1]*len(line)
        for cols, cell in enumerate(line):
            if cell == "#": row[cols] = 0
            elif cell == "S": start_position = (cols, rows)
            elif cell == "E": end_position = (cols, rows)
        map_grid.append(row)
        rows += 1
    
    bounds = (len(map_grid[0]), rows)

class Cell():
    x = 0
    y = 0
    direction = (1, 0)
    total_cost = 0
    parent = None

    def __init__(self, total_cost=0, x=0, y=0, direction=(1, 0), parent=None):
        self.total_cost = total_cost
        self.x = x
        self.y = y
        self.direction = direction
        self.parent = parent
    
    def diff(self, pos):
        x, y = (0, 0)
        if isinstance(pos, Cell):
            x = pos.x
            y = pos.y
        else:
            x = pos[0]
            y = pos[1]

        return (x - self.x, y - self.y)
    
    def add(self, pos):
        return (pos[0] + self.x, pos[1] + self.y)
    
    def _get_pos(self):
        return (self.x, self.y)
    
    def _set_pos(self, pos):
        if isinstance(pos, Cell):
            self.x = pos.x
            self.y = pos.y
        else:
            self.x = pos[0]
            self.y = pos[1]
    
    pos = property(_get_pos, _set_pos)

def in_bounds(cell:tuple, bounds:tuple):
    return 0 <= cell[0] < bounds[0] and 0 <= cell[1] < bounds[1]

# Do the magic here
def solve(start, end, map_grid, step_cost=1, turn_cost=1000):
    pos = start
    previous_cell = None
    
    check_cells = [Cell(0, *start)]
    visited_cells = set()

    best_path_cells = set()
    best_cost = 0

    while check_cells:
        cell = check_cells.pop(0)
        
        # Check if we've reached the end.
        if cell.pos == end:
            path = []
            best_cost = cell.total_cost
        
        if best_cost and cell.total_cost == best_cost:
            best_cell = cell
            while best_cell.parent:
                best_path_cells.add(best_cell.pos)
                best_cell = best_cell.parent
        
        # Add the cells to check.
        for direction in [cell.direction] + directions[cell.direction]:
            check_pos = cell.add(direction)
            
            if in_bounds(check_pos, bounds) and map_grid[check_pos[1]][check_pos[0]] and check_pos not in visited_cells:
                check_cost = cell.total_cost + step_cost + (0 if direction == cell.direction else turn_cost)
                check_cell = Cell(check_cost, *check_pos, direction, cell)

                inserted = False
                for i in range(len(check_cells)):
                    if check_cost < check_cells[i].total_cost:
                        check_cells.insert(i, check_cell)
                        inserted = True
                        break

                if not inserted: check_cells.append(check_cell)

        
        visited_cells.add(cell.pos)
    return (best_cost, best_path_cells)

solve_a, path = solve(start_position, end_position, map_grid)
solve_b = len(path)

for y, row in enumerate(map_grid):
    row_str = ""
    for x, cell in enumerate(row):
        row_str += "." if (x, y) in path else " " if cell else "#"
    print(row_str)

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a[test - 1] else f'Fail (expected {expected_a[test - 1]}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b[test - 1] else f'Fail (expected {expected_b[test - 1]}, got {solve_b}).'}" if test else solve_b)