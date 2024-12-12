test = 0
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

# Do the checksum
solve_a = sum(list(map(lambda x: x[0] * x[1], enumerate(fragmented_filesystem))))

# For Solve B - Contiguous at the cost of compression
data_block, free_block = analyze_filesystem(filesystem)
file_id = 1
last_file_id = len(data_block) - 1

# Rebuild the filesystem
new_filesystem = [(0, data_block.pop(0))]
while data_block or free_block:
    if free_block: new_filesystem.append((-1, free_block.pop(0)))
    if data_block:
        new_filesystem.append((file_id, data_block.pop(0)))
        file_id += 1

data_block, free_block = analyze_filesystem(filesystem)

# Start with the last file and work backwards
current_file_id = last_file_id
while current_file_id:
    # Grab our file and search for a suitable empty space as close to the start of the filesystem.
    current_file_size = data_block[current_file_id]
    file_index = new_filesystem.index((current_file_id, current_file_size))

    for search_index, block in enumerate(new_filesystem):
        # Check if we reached our file. If so, we couldn't find a spot closer.
        if search_index == file_index: break

        # Check if the block we are currently looking at is a free (-1) block, and has enough space.
        if block[0] == -1 and block[1] >= current_file_size:
            # Reduce the size of the free block by the size of our file.
            new_filesystem[search_index] = (-1, block[1] - current_file_size)

            # Convert our previous filesystem entry into free space.
            new_filesystem[file_index] = (-1, current_file_size)

            # Insert our file in front of the free space.
            new_filesystem.insert(search_index, (current_file_id, current_file_size))
            break
    current_file_id -= 1

# Do the checksum
current_block_index = 0
print(new_filesystem)
for block in new_filesystem:
    for count in range(block[1]):
        solve_b += (block[0] * current_block_index) if block[0] != -1 else 0
        current_block_index += 1

print(solve_a)
print(solve_b)
