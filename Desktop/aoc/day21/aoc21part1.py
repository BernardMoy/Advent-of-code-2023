with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

vlen = len(lines)
hlen = len(lines[0])

steps = 64

# Find the starting position
start = (0,0)

for i in range(vlen):
    for j in range(hlen):
        if lines[i][j] == 'S':
            start = (i,j)

print(start)

# Function to spread the existing explored tiles
def spread(explored):
    print(len(explored))
    for i in range(len(explored)):
        # Dequeue
        pos = explored[0]
        explored = explored[1::]

        # Spread the pos
        if pos[0]>0 and lines[pos[0]-1][pos[1]] == '.':
            explored.append((pos[0]-1, pos[1]))

        if pos[0]<vlen-1 and lines[pos[0]+1][pos[1]] == '.':
            explored.append((pos[0]+1, pos[1]))

        if pos[1]<hlen-1 and lines[pos[0]][pos[1]+1] == '.':
            explored.append((pos[0],pos[1]+1))

        if pos[1]>0 and lines[pos[0]][pos[1]-1] == '.':
            explored.append((pos[0],pos[1]-1))
    
    return explored

explored = [start]
for i in range(steps):
    explored = list(set(spread(explored)))

print('Answer -> ' + str(len(explored) + 1))

