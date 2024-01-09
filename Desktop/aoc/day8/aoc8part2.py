import math

with open ('aoc8.txt', 'r') as file:
    lines = file.read().split('\n')

instructions = lines[0]

# Dictionary to store the search routes
dict = {}
# Extract all nodes ending with A
node = []

for line in lines[2::]:
    line.replace(" ", "")
    route = line.split(' = ')
    dict[route[0]] = route[1]

    if route[0][2] == 'A':
        node.append(route[0])


# Return the number of steps needed to reach nodes ending with Z.
def func(current):
    i = 0   # number of steps performed
    # Perform the search actions until we reach ZZZ
    while current[2] != 'Z':
        if instructions[i % len(instructions)] == 'L':
            current = dict[current][1:4]
        else:
            current = dict[current][6:9]
        i+=1

    return i


# Extract all nodes ending with A
result = []
for i in range(len(node)):
    result.append(func(node[i]))

print((result))

# The answer is equal to the LCM of all numbers in result
# Extract the contents of the list with (*)
print(math.lcm(*result))
