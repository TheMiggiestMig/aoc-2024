import io
test = 1
test_data = io.StringIO(
"""
Put your test data here
This is more data
This is a third line
"""
)
test_data.readline() # Get rid of the first empty line (it's only there for display purposes).

solve_a = 0
solve_b = 0
expected_a = 420
expected_b = 9001

# Parse the input and provide as many outputs as required.
with test_data if test else open("data") as f:
    line = f.readline().strip()

    while line:
        # Parse the file line by line.
        print(line)
        line = f.readline().strip()

# Do the magic here

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)