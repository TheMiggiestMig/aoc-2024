test = 0
file = 'test' if test else 'data'

solve_a = 0
solve_b = 0

import re
import time

operations = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "/": lambda x, y: x // y,
    "-": lambda x, y: x - y
}
equations = []

# Parse the file
with open(file) as f:
    line = f.readline().strip()
    
    while line:
        expected, values = line.split(": ")
        expected = int(expected)
        values = [int(value) for value in values.split(" ")]
        
        equations.append({
            "expected": expected,
            "values": values
        })
        
        line = f.readline().strip()

def resolve(expected_result, values, current_result=None):
    result = False
    
    if current_result is None:
        current_result = values[0]
        values = values[1:]
    
    if not values: return current_result == expected_result
    
    for operation in operations:
        result = result or resolve(expected_result, values[1:], operations[operation](current_result, values[0]))
        if result:
            print(f"Found matching result for {expected_result}")
            time.sleep(0.0001)
            return True
    
    return result
    
for equation in equations:
    solve_a += equation["expected"] if resolve(equation["expected"], equation["values"]) else 0

print(solve_a)
print(solve_b)
