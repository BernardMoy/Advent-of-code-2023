with open('input.txt', 'r') as file:
    lines = file.read().split('\n')


# Find the rightmost and leftmost coord
maxright = 0
maxleft = 0
maxup = 0
maxdown = 0
coordH = 0
coordV = 0

for line in lines:
    line = line.split(' ')
    if line[0] == 'R':
        coordH += int(line[1])
        if coordH > maxright:
            maxright = coordH
    if line[0] == 'L':
        coordH -= int(line[1])
        if coordH < maxleft:
            maxleft = coordH
    if line[0] == 'D':
        coordV += int(line[1])
        if coordV > maxdown:
            maxdown = coordV 
    if line[0] == 'U':
        coordV -= int(line[1])
        if coordV < maxup:
            maxup = coordV 

print((maxleft, maxright, maxup, maxdown))
board = [['.' for _ in range(abs(maxleft) + abs(maxright)+1)] for _ in range(abs(maxup) + abs(maxdown)+1)]
board[abs(maxup)][abs(maxleft)] = '#'

current = (abs(maxup), abs(maxleft))

# Process the board
# Count = number of # in rings
count = 0

for line in lines:
    direction = line.split(' ')[0]
    number = int(line.split(' ')[1])

    for i in range(number):
        if direction == 'R':
            current = (current[0], current[1]+1)
            board[current[0]][current[1]] = '#'
            count+=1
        if direction == 'L':
            current = (current[0], current[1]-1)
            board[current[0]][current[1]] = '#'     
            count+=1  
        if direction == 'U':
            current = (current[0]-1, current[1])
            board[current[0]][current[1]] = '#'
            count+=1
        if direction == 'D':
            current = (current[0]+1, current[1])
            board[current[0]][current[1]] = '#' 
            count+=1

# Find an element that is inside the grid
def findInside(board):
    for i in range(len(board)):
      for j in range(len(board[i])):
          if j>len(board[i])-2:
             continue 
          if board[i][j] == '#' and board[i][j+1] == '.':
              return (i,j+1)
    
    return None

# Find the number of spaces inside it
number = 0

start = findInside(board)

walls = []
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '#':
            walls.append((i,j))

print(walls)

