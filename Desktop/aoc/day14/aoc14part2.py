with open('input.txt', 'r') as file:
    lines = file.read().split('\n')


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

def tiltNorth(lines):
    new_lines = []

    # Transpose it
    columns = list(zip(*lines))

    for col in columns:
        val = 0
        new = []

        # Fill the array with dots
        for i in range(len(col)):
            new.append('.')

        for i in range(len(col)):
            if col[i] == 'O':
                new[val] = 'O'
                val += 1
            if col[i] == '.':
                continue
            if col[i] == '#':
                new[i] = '#'
                val = i+1
        
        new_lines.append(new)

    # Transpose it
    new_lines = list(zip(*new_lines))

    return new_lines


def tiltSouth(lines):
    new_lines = []

    lines.reverse()

    # Transpose it
    columns = list(zip(*lines))

    for col in columns:
        val = 0
        new = []

        # Fill the array with dots
        for i in range(len(col)):
            new.append('.')

        for i in range(len(col)):
            if col[i] == 'O':
                new[val] = 'O'
                val += 1
            if col[i] == '.':
                continue
            if col[i] == '#':
                new[i] = '#'
                val = i+1
        
        new_lines.append(new)

    # Transpose it
    new_lines = list(zip(*new_lines))

    new_lines.reverse()

    return new_lines


def tiltWest(lines):
    new_lines = []

    for row in lines:
        val = 0
        new = []

        # Fill the array with dots
        for i in range(len(row)):
            new.append('.')

        for i in range(len(row)):
            if row[i] == 'O':
                new[val] = 'O'
                val += 1
            if row[i] == '.':
                continue
            if row[i] == '#':
                new[i] = '#'
                val = i+1
        
        new_lines.append(new)

    return new_lines


def tiltEast(lines):
    new_lines = []


    for row in lines:

        row = row[::-1]

        val = 0
        new = []

        # Fill the array with dots
        for i in range(len(row)):
            new.append('.')

        for i in range(len(row)):
            if row[i] == 'O':
                new[val] = 'O'
                val += 1
            if row[i] == '.':
                continue
            if row[i] == '#':
                new[i] = '#'
                val = i+1
        
        new_lines.append(new[::-1])

    return new_lines


def cycle(lines):
    new = tiltEast(tiltSouth(tiltWest(tiltNorth(lines))))

    return new

# Find sum
def sum(lines):
    total = 0
    for i in range(len(lines)):
        for j in lines[i]:
            if j == 'O':
                total += len(lines) - i
    
    return total



# Find the number of cycles that forms a loop
# Then we can ignore all repeated cycles within that loop
history = [lines]

new = cycle(lines)

while (new not in history):
    history.append(new)
    new = cycle(new)


index = history.index(new)
# Length of loop
print(len(history))

# Number of cycles needed
number = ((1000000000- index) % (len(history) - index))

# Index + modulus after ignoring all intermediate cycles
for i in range(number + index):
    lines = cycle(lines)

print(sum(lines))