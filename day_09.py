test = 1
file = 'test' if test else 'data'

solve_a = 0
solve_b = 0

filesystem = ""
data_block = []
free_block = []
file_id = 0
last_file_id = -1

# Parse the file
with open(file) as f:
    filesystem = f.readline().strip()

def analyze_filesystem(filesystem):
    data = [int(block) for block in filesystem[::2]]
    free = [int(block) for block in filesystem[1::2]]
    
    return data, free

# For Solve A - Compression at the cost of fragmentation
data_block, free_block = analyze_filesystem(filesystem)
file_id = 0
last_file_id = len(data_block) - 1

fragmented_filesystem = []

# Fragment the sucker!
while data_block:
    fragmented_filesystem += [file_id] * data_block.pop(0)
    if not data_block: break
    
    free_space = free_block.pop(0)
    while free_space:
        if not data_block: break
    
        if data_block[-1] <= free_space:
            amount = data_block.pop()
            fragmented_filesystem += [last_file_id] * amount
            last_file_id -= 1
        else:
            amount = free_space
            data_block[-1] -= amount
            fragmented_filesystem += [last_file_id] * amount
        free_space -= amount
        
    file_id += 1

# For Solve B - Contiguous at the cost of compression
data_block, free_block = analyze_filesystem(filesystem)
file_id = 0
last_file_id = len(data_block) - 1

# Lets use a double-linked list, because we can.

class Block():
    def __init__(self, int file_id, int size, bool free, prev_block=None, next_block=None):
        self.id = file_id
        self.size = size
        self.free = free
        self.previous_block = prev_block
        self.next_block = next_block
    
    def next(self, next_block=None):
        if next_block: self.next_block = next_block
        return self.next_block or False
    
    def previous(self, prev_block=None):
        if prev_block: self.prev_block = prev_block
        return self.prev_block or False

test = Block(0, 2, False)
print(test)
    

# Tetris it a bit!
while data_block:
    fragmented_filesystem += [file_id] * data_block.pop(0)
    if not data_block: break
    
    free_space = free_block.pop(0)
    while free_space:
        if not data_block: break
    
        if data_block[-1] <= free_space:
            amount = data_block.pop()
            fragmented_filesystem += [last_file_id] * amount
            last_file_id -= 1
        else:
            amount = free_space
            data_block[-1] -= amount
            fragmented_filesystem += [last_file_id] * amount
        free_space -= amount
        
    file_id += 1

solve_a = sum(list(map(lambda x: x[0] * x[1], enumerate(fragmented_filesystem))))
solve_b = 0

print(solve_a)
print(solve_b)
