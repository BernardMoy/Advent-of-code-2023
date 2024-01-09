# DIFFICULT

import copy

with open ('aoc10.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = list(lines[i])

# Horizontal and vertical dimensions
horizontal = len(lines[0])
vertical = len(lines)

# Output is converted into numbers
output = copy.deepcopy(lines)

start_coord = None

# Find the start coord
for i in range(vertical):
    for j in range(horizontal):
        if lines[i][j] == 'S':
            start_coord = (i, j)
            output[i][j] = 0
walls = []

affected = [start_coord]

# Given a coordinate, spread its path to the output list.
# Returns coords that have been affected.
def spread(coords):
    saved_coords = copy.deepcopy(coords)

    # A list of affected coords (i,j)
    affected.clear()

    for i, j in saved_coords:
        # F
        if lines[i][j] == 'F':
            if down(i, j):
                affected.append ((i+1, j))
    
            if right(i, j):
                affected.append ((i, j+1))
    
                                    
        # J
        if lines[i][j] == 'J':
            if left(i, j):
                affected.append ((i, j-1))
    
            if up(i, j):
                affected.append ((i-1, j))
    

        # 7
        if lines[i][j] == '7':
            if left(i, j):
                affected.append ((i, j-1))
    
            if down(i, j):
                affected.append ((i+1, j))
    
        # L
        if lines[i][j] == 'L':
            if up(i, j):
                affected.append ((i-1, j))
    
            if right(i, j):
                affected.append ((i, j+1))
    
        # |
        if lines[i][j] == '|':
            if up(i, j):
                affected.append ((i-1, j))
    
            if down(i, j):
                affected.append ((i+1, j))
    
        # -
        if lines[i][j] == '-':
            if left(i, j):
                affected.append ((i, j-1))
    
            if right(i, j):
                affected.append ((i, j+1))
    

        # S --> All 4 directions
        if lines[i][j] == 'S':
            if up(i, j):
                affected.append ((i-1, j))
    
            if down(i, j):
                affected.append ((i+1, j))
    
            if left(i, j):
                affected.append ((i, j-1))
    
            if right(i, j):
                affected.append ((i, j+1))
    

    


def down(i, j):
    if i < vertical-1:
        if output[i+1][j] in ['L', 'J', '|']:
            output[i+1][j] = output[i][j] + 1
            return (i+1, j)
    return None

def up(i, j):
    if i > 0:
        if output[i-1][j] in ['F', '7', '|']:
            output[i-1][j] = output[i][j] + 1
            return (i-1, j)
    return None

def left(i, j):
    if j > 0:
        if output[i][j-1] in ['F', 'L', '-']:
            output[i][j-1] = output[i][j] + 1
            return (i, j-1)
    return None

def right(i, j):
    if j < horizontal -1:
        if output[i][j+1] in ['7', 'J', '-']:
            output[i][j+1] = output[i][j] + 1
            return ((i, j+1))
    return None


while(len(affected) != 0):
    spread(affected)
    walls = walls + affected


max = 0
for i in range(vertical):
    for j in range(horizontal):
        if str(output[i][j]).isdigit() and int(output[i][j]) > int(max):
            max = output[i][j]

print(max)
