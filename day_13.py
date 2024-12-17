import io
test = 1
test_data = io.StringIO(
"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
)
test_data.readline() # Get rid of the first empty line (it's only there for display purposes).

solve_a = 0
solve_b = 0
expected_a = 100
expected_b = 0

# Parse the input and provide as many outputs as required.
machines = []

with test_data if test else open("data") as file:
    machine = {}
    for line in file:
        if not line.strip():
            machines.append(machine)
            machine = {}
        elif line[:1] == "P":
            machine["Prize"] = tuple(int(value.split("=")[1]) for value in line[7:].split(", "))
        else:
            machine[line[7]] = tuple(int(value.split("+")[1]) for value in line[10:].split(", "))

# Do the magic here

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)
