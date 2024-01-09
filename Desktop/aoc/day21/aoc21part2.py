with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

vlen = len(lines)
hlen = len(lines[0])


# Find the starting position
start = (0,0)

for i in range(vlen):
    for j in range(hlen):
        if lines[i][j] == 'S':
            start = (i,j)

print(start)




# Find all reachable points
explored = []
current = [start]

while len(current) != 0:
    # Dequeue
    pos = current[0]
    current = current[1::]

    if pos in current or pos in explored:
        continue 

     # Spread the pos
    if pos[0]>0 and lines[pos[0]-1][pos[1]] == '.' and (pos[0]-1, pos[1]) not in explored:
        current.append((pos[0]-1, pos[1]))

    if pos[0]<vlen-1 and lines[pos[0]+1][pos[1]] == '.' and (pos[0]+1, pos[1]) not in explored:
        current.append((pos[0]+1, pos[1]))

    if pos[1]<hlen-1 and lines[pos[0]][pos[1]+1] == '.' and (pos[0],pos[1]+1) not in explored:
        current.append((pos[0],pos[1]+1))

    if pos[1]>0 and lines[pos[0]][pos[1]-1] == '.' and (pos[0],pos[1]-1) not in explored:
        current.append((pos[0],pos[1]-1))

    # FInished exploring
    explored.append(pos)

print(len(explored))



# Squares filled only with odd parity
def oddcount():
    dots = [(i,j) for (i,j) in explored if (i+j)%2 == 1]
    return len(dots)

# Squares filled only with even parity
def evencount():
    dots = [(i,j) for (i,j) in explored if (i+j)%2 == 0]
    return len(dots)

def oddcorner():
    dots = [(i,j) for (i,j) in explored if (i+j)%2 == 1 and abs(i-65)+abs(j-65)>65]
    return len(dots)

def evencorner():
    dots = [(i,j) for (i,j) in explored if (i+j)%2 == 0 and abs(i-65)+abs(j-65)>65]
    return len(dots)


print(oddcount())
print(evencount())
print(oddcorner())
print(evencorner())

# Use a grid paper to draw four lines between the topmost, bottommost, leftmost and rightmost points.
# The middle areas are reachable.
print((202301)**2 * oddcount() + (202300)**2 * evencount() - (202301)*oddcorner() + (202300)*evencorner())

