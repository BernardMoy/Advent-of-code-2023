with open ('aoc8.txt', 'r') as file:
    lines = file.read().split('\n')

instructions = lines[0]

# Dictionary to store the search routes
dict = {}

for line in lines[2::]:
    line.replace(" ", "")
    route = line.split(' = ')
    dict[route[0]] = route[1]


current = 'AAA'
i = 0   # number of steps performed
# Perform the search actions until we reach ZZZ
while current != 'ZZZ':
    if instructions[i % len(instructions)] == 'L':
        current = dict[current][1:4]
    else:
        current = dict[current][6:9]
    i+=1

print(i)    
