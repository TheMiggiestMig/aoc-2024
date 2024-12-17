import io
import re

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
expected_a = 480
expected_b = 875318608908

# Parse the input and provide as many outputs as required.
machines = []

with test_data if test else open("data") as file:
    machines_raw = file.read().split("\n\n")
    for machine in machines_raw:
        ax ,ay, bx, by, px, py = map(lambda n: int(n), re.findall(r"\d+", machine))
        machines.append(((ax ,ay), (bx, by), (px, py)))

solve_b_base = 10000000000000

# Do the magic here
def solve(base=0):
    result = 0
    for machine in machines:
        # Linear algebra and simultaneous equations!
        ax, ay = machine[0]
        bx, by = machine[1]
        px, py = machine[2]

        if base: px, py = (px + base, py + base)

        num_b = (ax * py) - (ay * px)
        den_b = (ax * by) - (ay * bx)

        b = num_b // den_b
        mod_b = num_b % den_b

        num_a = px - (bx * b)
        a = num_a // ax

        mod_a = num_a % ax

        result += 0 if mod_a or mod_b else (a *3 + b)
    
    return result

solve_a = solve()
solve_b = solve(solve_b_base)

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)
