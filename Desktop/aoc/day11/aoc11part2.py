from turtle import distance


with open ('aoc11.txt', 'r') as file:
    lines = file.read().split('\n')

for t in range(len(lines)):
    lines[t] = list(lines[t])

empty_rows = []
empty_columns = []

# Expand rows
i = 0
while i < len(lines):
    if all(lines[i][j] == '.' for j in range(len(lines[i]))):
        empty_rows.append(i)
    i += 1

# Expand columns
j = 0
while j < len(lines[0]):
    if all(lines[i][j] == '.' for i in range(len(lines))):
        empty_columns.append(j)
    j+=1

print(lines)

galaxy = []

for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == '#':
            galaxy.append((x,y))

print(len(galaxy))



# Return the distance between two tuples
def dist(t1, t2):
    multiplier = 1000000

    # Count the number of expanded rows and columns within the range of two points
    countrow = len([item for item in empty_rows if item > min(t1[0], t2[0]) and item < max(t1[0], t2[0])])
    countcol = len([item for item in empty_columns if item > min(t1[1], t2[1]) and item < max(t1[1], t2[1])])
    
    # Add the expanded rows and cols to the final result
    return abs(t2[1]-t1[1])+abs(t2[0]-t1[0]) + (multiplier-1)*(countrow + countcol)



distances = []

for i in range(len(galaxy)):
    for j in range(i, len(galaxy)):
        distances.append(dist(galaxy[i], galaxy[j]))

print(sum(distances))
