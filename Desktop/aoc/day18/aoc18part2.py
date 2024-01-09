with open('input.txt', 'r') as file:
    lines = file.read().split('\n')


# Edit the lines to match correct format
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')

    if lines[i][2][7] == '0':
        lines[i][0] = 'R'
    if lines[i][2][7] == '1':
        lines[i][0] = 'D'
    if lines[i][2][7] == '2':
        lines[i][0] = 'L'
    if lines[i][2][7] == '3':
        lines[i][0] = 'U'
    
    lines[i][1] = int(lines[i][2][2:7], 16)



# Old code
vertex = [(0,0)]

current = (0,0)

count = 0

for line in lines:

    if line[0] == 'R':
        current = (current[0], current[1] + int(line[1]))
        vertex.append(current)

    if line[0] == 'L':
        current = (current[0], current[1] - int(line[1]))
        vertex.append(current)

    if line[0] == 'D':
        current = (current[0] + int(line[1]), current[1])
        vertex.append(current)

    if line[0] == 'U':
        current = (current[0] - int(line[1]), current[1])
        vertex.append(current)
    
    count += int(line[1])

# Shoelace formula: Coordinates --> Area
area = 0
for i in range(0, len(vertex)-1):
    area += vertex[i][0]*vertex[i+1][1] - vertex[i+1][0]*vertex[i][1]
area += vertex[-1][0]*vertex[0][1] - vertex[0][1]*vertex[-1][0]

area = 1/2*abs(area)

print(area)

# Count = number of boundary items
# A = i + b/2 -1
print(count)
print((2*(int(area)+1) - count)/2 + count)