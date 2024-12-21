import io
import re

test = 0
test_data = io.StringIO(
"""
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
)
test_data.readline() # Get rid of the first empty line (it's only there for display purposes).

solve_a = 0
solve_b = 0
expected_a = "4,6,3,5,6,3,5,2,1,0"
expected_b = 9001

# Parse the input and provide as many outputs as required.
ip = 0
reg = []
data = []
stdout = []

def combo(value):
    global ip
    if value in [0,1,2,3]: return value
    if value == 4: return reg[0]
    if value == 5: return reg[1]
    if value == 6: return reg[2]
    if value == 7: raise Exception("opcode of 7 is reserved")

def op_adv(reg, data):
    global ip
    reg[0] = reg[0] >> combo(data[ip + 1])
    ip += 2

def op_bxl(reg, data):
    global ip
    reg[1] = reg[1] ^ data[ip + 1]
    ip += 2

def op_bst(reg, data):
    global ip
    reg[1] = combo(data[ip + 1]) % 8
    ip += 2

def op_jnz(reg, data):
    global ip
    if reg[0]:
        if data[ip + 1] > len(data): raise Exception("SEGFAULT")
        ip = data[ip + 1]
    else:
        ip += 2

def op_bxc(reg, data):
    global ip
    reg[1] = reg[1] ^ reg[2]
    ip += 2

def op_out(reg, data):
    global ip
    global stdout
    stdout.append(combo(data[ip + 1]) % 8)
    ip += 2

def op_bdv(reg, data):
    global ip
    reg[1] = reg[0]  >> combo(data[ip + 1])
    ip += 2

def op_cdv(reg, data):
    global ip
    reg[2] = reg[0]  >> combo(data[ip + 1])
    ip += 2

opcodes = [
    op_adv,
    op_bxl,
    op_bst,
    op_jnz,
    op_bxc,
    op_out,
    op_bdv,
    op_cdv
]

with test_data if test else open("data") as file:
    for line in file:
        if not line.strip(): break
        reg.append(int(re.findall(r"\d+", line)[0]))
    data = [int(num) for num in re.findall(r"\d+", file.readline())]

# Do the magic here
# solve A
while True:
    if ip >= len(data):
        solve_a = ",".join([str(num) for num in stdout])
        break
    opcodes[data[ip]](reg, data)

# solve B
solve_b = 0

def reset():
    global stdout
    global reg
    global ip

    stdout = []
    reg = [solve_b, 0, 0]
    ip = 0

found = False
while True:
    if ip >= len(data):
        solve_b += 1
        reset()
    opcodes[data[ip]](reg, data)

    if data[ip - 2] == 5: # If the opcode we just executed was 'out'
        if not solve_b % 1000: print(solve_b,data,stdout, "\r", end="")
        for i, value in enumerate(stdout):
            if stdout[i] != data[i]:
                solve_b += 1
                reset()
            elif len(stdout) == len(data):
                found = True
                break
    if found: break

print(f"[ DEBUG ] {f'PASS! ({solve_a})' if solve_a == expected_a else f'Fail (expected {expected_a}, got {solve_a}).'}" if test else solve_a)
print(f"[ DEBUG ] {f'PASS! ({solve_b})' if solve_b == expected_b else f'Fail (expected {expected_b}, got {solve_b}).'}" if test else solve_b)
