test = 0
file = 'test' if test else 'data'

solve_a = 0
solve_b = 0
expected_a = 1930
expected_b = 1206

# Parse the input and provide as many outputs as required.
def parse_input(file):
    with open(file) as f:
        line = f.readline().strip()
    
    return parsed_input

# Do the magic here
parsed_input = parse_input(file)



print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)