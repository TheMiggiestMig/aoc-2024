test = 0
file = 'test' if test else 'data'

solve_a = 0
solve_b = 0

from itertools import permutations

antennas = {}
bounds = (0,0)

# Parse the file
with open(file) as f:
    line = f.readline().strip()
    row = 0
    bound_x = len(line)
    
    while line:
        for column, cell in enumerate(line):
            if cell != '.':
                antennas[cell] = antennas[cell] + [(column, row)] if cell in antennas.keys() else [(column, row)]
        row += 1
        line = f.readline().strip()
    
    bounds = (bound_x, row)

in_bounds = lambda x: 0 <= x[0] < bounds[0] and 0 <= x[1] < bounds[1]

def do_mark(nodes, resonate=False):
    node_pairs = permutations(nodes,2)
    for a, b in node_pairs:
        diff = (a[0] - b[0], a[1] - b[1])
        resonance = 1
        mark = (a[0] + (diff[0] * resonance), a[1] + (diff[1] * resonance))
        
        if resonate: marked[a] = True
        
        while in_bounds(mark):
            
            marked[mark] = True
            
            if not resonate: break
            
            resonance += 1
            mark = (a[0] + (diff[0] * resonance), a[1] + (diff[1] * resonance))

marked = {}
for nodes in antennas.values():
    do_mark(nodes)
print(len(list(marked.keys())))

marked = {}
for nodes in antennas.values():
    do_mark(nodes, True)
print(len(list(marked.keys())))