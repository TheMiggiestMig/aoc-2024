test = False
file = 'test' if test else 'data'

solveA = 0
solveB = 0

import itertools

def follow(needle, haystack, start, search_vector):
    if haystack[start[1]][start[0]] == needle[0]:
        if needle[1:] == "": return True
        
        next_x = start[0] + search_vector[0]
        next_y = start[1] + search_vector[1]
        
        if 0 <= next_x < len(word_search[0]) and 0 <= next_y < len(word_search):
            return follow(needle[1:], haystack, (next_x, next_y), search_vector)
        
    return False

word_search = []

with open(file) as f:
    line = f.readline()
    
    while line:
        word_search.append(line.strip())
        line = f.readline()


vectors = list(set(itertools.permutations([-1,0,1,-1,1], 2))) # Because I'm lazy

for y, row in enumerate(word_search):
    for x, char in enumerate(row):
        if char == "X":
            for vector in vectors:
                found = follow("XMAS", word_search, (x,y), vector)
                solveA += 1 if found else 0
        elif char == "A":
            if 0 < x < len(row) - 1 and 0 < y < len(word_search) - 1:
                check = word_search[y-1][x-1] + word_search[y-1][x+1] + word_search[y+1][x-1] + word_search[y+1][x+1]
                solveB += 1 if check in ("MSMS", "MMSS", "SMSM", "SSMM") else 0   # Janky AF, I know. I wanna go home :(

print(solveA)
print(solveB)
