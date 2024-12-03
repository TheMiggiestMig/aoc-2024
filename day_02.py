test = False
file = 'test' if test else 'data'
# Online Python - IDE, Editor, Compiler, Interpreter

errorTolerance = 1
solveA = 0
solveB = 0

def check(line, tolerance=0):
    # Everthing about this challenge is based on the differences between sequencial numbers.
    # Lets work with those.
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    
    # Make sure we actually have a sign (upward or downward sequence)
    sumDiffs = sum(diffs)
    if sumDiffs == 0: return 0
    
    sign = sumDiffs // abs(sumDiffs)
    
    for i, x in enumerate(diffs):
        # Check that each difference is in the same direction (sign) as the majority of the sequence.
        # Also make sure that it is between 1 and 3.
        if not 1 <= x * sign <= 3:
            
            # Do we have a tolerance for one error? If so, check possible lines by removing an element.
            if tolerance:
                errorCheck = 0 or check(line[:i] + line[i + 1:], tolerance - 1) # It might be this element
                if not errorCheck and i < len(line) - 1:
                    errorCheck = check(line[:i + 1]+line[i + 2:], tolerance - 1) # If not, it might be the next element
                    
                return errorCheck
            return 0
    return 1

# Read each line and check if good.
with open(file) as f:
    line = f.readline()
    
    while line:
        # Do something
        parsedLine = [int(x) for x in line.split(" ")]
        good = check(parsedLine)
        
        solveA += good
        solveB += good or check(parsedLine, errorTolerance)
        
        line = f.readline()

print(solveA)
print(solveB)
