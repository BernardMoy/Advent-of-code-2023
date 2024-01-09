from turtle import distance


with open ('aoc11.txt', 'r') as file:
    lines = file.read().split('\n')

for t in range(len(lines)):
    lines[t] = list(lines[t])


# Expand rows
i = 0
while i < len(lines):
    if all(lines[i][j] == '.' for j in range(len(lines[i]))):
        lines = lines[0:i+1:] + [lines[i]] + lines[i+1:len(lines):]
        i+=1
    i += 1

# Expand columns
j = 0
while j < len(lines[0]):
    if all(lines[i][j] == '.' for i in range(len(lines))):
        for k in range(len(lines)):
            lines[k] = lines[k][0:j+1:] + [lines[k][j]] + lines[k][j+1:len(lines[k]):]
        j+=1
    j+=1

print(lines)

galaxy = []

for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == '#':
            galaxy.append((x,y))

print(len(galaxy))
distances = []

for i in range(len(galaxy)):
    for j in range(i, len(galaxy)):
        distances.append(abs(galaxy[i][1]-galaxy[j][1])+abs(galaxy[i][0]-galaxy[j][0]))

print(sum(distances))