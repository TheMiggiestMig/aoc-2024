test = 0
file = 'test' if test else 'data'

solve_a = 0
solve_b = 0

rules = {}
print_orders = []

import functools

with open(file) as f:
    # Read the rules
    line = f.readline().strip()
    
    while line:
        rule = [int(rule) for rule in line.split("|")]
        
        if rule[0] not in rules.keys(): rules[rule[0]] = []
        if rule[1] not in rules.keys(): rules[rule[1]] = []
        
        rules[rule[0]].append(rule[1])
        
        line = f.readline().strip()
    
    # Read the print orders
    line = f.readline().strip()
    
    while line:
        print_orders.append([int(page) for page in line.split(",")])
        
        line = f.readline().strip()

for order in print_orders:
    score = order[(len(order) - 1) // 2]
    
    # Solve A
    for page_index, page in enumerate(order):
        if(list(set(order[:page_index]) & set(rules[page]))):
            score = 0
            break
    solve_a += score
    
    # Solve B
    if not score:
        corrected_order = sorted(order, key=functools.cmp_to_key(lambda x, y: -1 if y in rules[x] else 1))
        solve_b += corrected_order[(len(corrected_order) - 1) // 2]

print(solve_a)
print(solve_b)
