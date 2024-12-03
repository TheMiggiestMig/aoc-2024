test = False
file = 'test' if test else 'data'

solveA = 0
solveB = 0

import re
with open(file) as f:
    mulFlag = True
    data = f.read()
    
    # Extract all the muls.
    items = re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data)
    
    for item in items:
        if item[0][:3] == "mul":
            mul = int(item[1]) * int(item[2])
            solveA += mul
            if mulFlag: solveB += mul
        elif item[0][:3] == "don":
            mulFlag = False
        else:
            mulFlag = True
            
print(solveA)
print(solveB)
