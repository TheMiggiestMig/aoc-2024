test = False
file = 'test' if test else 'data'

solveA = 0
solveB = 0

import re

with open(file) as f:
    leftValues = []
    rightValues = []
    
    line = f.readline()
    
    while line:
        a, b =[int(x) for x in (re.findall("\d+", line))]
        leftValues.append(a)
        rightValues.append(b)
        
        line = f.readline()
    
    leftValues = sorted(leftValues)
    rightValues = sorted(rightValues)
    
    solveA = sum([b-a for a, b in zip(leftValues, rightValues)])
    
    keys = set(leftValues)
    solveB = sum([key * len(list(filter(lambda x: x == key, leftValues))) * len(list(filter(lambda x: x == key, rightValues))) for key in keys])
    
print(solveA)
print(solveB)
