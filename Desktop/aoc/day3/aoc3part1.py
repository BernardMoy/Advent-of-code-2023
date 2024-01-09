with open ('aoc3.txt', 'r') as file:
    lines = file.read().split('\n')

# Given indexes i, j in the lines 2D array, determine if the number starting from that index is adjacent to a symbol 
def is_adjacent(lines, i, j):
    symbols = ['=', '#', '%', '+', '$', '*', '-', '/','&','@']
    
    length = len(scan_number(lines, i, j))

    # Left side
    try:
        if lines[i][j-1] in symbols:
            return True
    except:
        pass
    try:
        if lines[i-1][j-1] in symbols:
            return True 
    except:
        pass
    try:
        if lines[i+1][j-1] in symbols:
            return True
    except:
        pass
    
    # Middle and right side
    for k in range(j, j+length+1):
        try:
            if lines[i-1][k] in symbols:
                return True 
        except:
            pass
        try:
            if lines[i+1][k] in symbols:
                return True
        except:
            pass
    
    # The direct right element to the end of the number
    try:
        if lines[i][j+length] in symbols:
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

                sum += int(scan_number(lines, i, j))
                print(scan_number(lines, i, j))

            # Move the pointer over that number
            j += (len(scan_number(lines, i, j)) -1)
            
        j+=1

print(sum)
