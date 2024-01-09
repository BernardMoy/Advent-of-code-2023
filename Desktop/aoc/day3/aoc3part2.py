with open ('aoc3.txt', 'r') as file:
    lines = file.read().split('\n')

store_coord = []
store_num = []

# Besides returning true, it also adds the (number, (i,j)) pair into store
# Given indexes i, j in the lines 2D array, determine if the number starting from that index is adjacent to a symbol 
def is_adjacent(lines, i, j):
    symbols = ['*']
    
    length = len(scan_number(lines, i, j))

    # Left side
    try:
        if lines[i][j-1] in symbols:
            store_num.append(scan_number(lines, i, j))
            store_coord.append((i,j-1))
            return True
    except:
        pass
    try:
        if lines[i-1][j-1] in symbols:
            store_num.append(scan_number(lines, i, j))
            store_coord.append((i-1,j-1))
            return True 
    except:
        pass
    try:
        if lines[i+1][j-1] in symbols:
            store_num.append(scan_number(lines, i, j))
            store_coord.append((i+1,j-1))
            return True
    except:
        pass
    
    # Middle and right side
    for k in range(j, j+length+1):
        try:
            if lines[i-1][k] in symbols:
                store_num.append(scan_number(lines, i, j))
                store_coord.append((i-1,k))
                return True 
        except:
            pass
        try:
            if lines[i+1][k] in symbols:
                store_num.append(scan_number(lines, i, j))
                store_coord.append((i+1,k))
                return True
        except:
            pass
    
    # The direct right element to the end of the number
    try:
        if lines[i][j+length] in symbols:
            store_num.append(scan_number(lines, i, j))
            store_coord.append((i, j+length))
            return True
    except:
        pass

    return False

# Given the first found digit, scan rightwards to find the whole number in the string
def scan_number(lines, i, j):
    if not lines[i][j].isdigit():
        return None
    
    num = lines[i][j]

    tmp = j+1

    # Scan rightwards to find the full number
    while tmp < len(lines[i]) and lines[i][tmp].isdigit():
        num += lines[i][tmp]
        tmp += 1

    return num

sum = 0


for i in range(len(lines)):
    j = 0
    while (j < len(lines[i])):
        
        if lines[i][j].isdigit():

            # The number beginning there is adjacent to a symbol
            if is_adjacent(lines, i, j):

                print(scan_number(lines, i, j))

            # Move the pointer over that number
            j += (len(scan_number(lines, i, j)) -1)
            
        j+=1


# Extract all numbers in store_coord where its coordinates has appeared exactly 2 times
counts = {}   # Store count of the coords

print(store_num)
print(store_coord)

for coord in store_coord:
    counts[coord] = counts.get(coord, 0) + 1   # Get the current count, default = 0

# Extract the front and rear index of coord that appeared 2 times
for coord, count in counts.items():
    if count == 2:
        print(coord)
        firstIndex = store_coord.index(coord)
        reverse_store_coord = store_coord.copy()
        reverse_store_coord.reverse()
        secondIndex = len(store_coord) - reverse_store_coord.index(coord) - 1

        print (firstIndex, secondIndex)
        # Get back the numbers, which will be at the same indices as the coordinates since they are added at the same time
        number = int(store_num[firstIndex]) * int(store_num[secondIndex])

        sum += number


print(sum)