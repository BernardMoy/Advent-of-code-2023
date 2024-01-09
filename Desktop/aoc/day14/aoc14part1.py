with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

# Transpose it
columns = list(zip(*lines))

# Find the sum of one column after tilting it to the LEFT
# Reset the pointer(val) to that index when a # is encountered
def func(col):
    sum = 0
    val = len(col)

    for i in range(len(col)):
        if col[i] == 'O':
            sum += val
            val -= 1
        if col[i] == '.':
            continue
        if col[i] == '#':
            val = len(col) - i - 1
    
    return sum

total = 0

for col in columns:
    
    total += func(col)
    print(func(col))

print(total)