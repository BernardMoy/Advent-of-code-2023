
with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

vlen = len(lines)
hlen = len(lines[0])

# Check if a pos is valid
history = set()

def valid(i, j):
    
    if i<0 or j<0:
        return False
    if i>vlen-1 or j>hlen-1:
        return False
    
    return True

def val(i,j):
    return int(lines[i][j])

memo = {}

# DP
def M(i,j,direction):

    # Reached the end
    if i==vlen-1 and j==hlen-1:
        return val(i,j)
    
    if (i,j,direction) in memo.keys():
        return memo[(i,j,direction)]
    
    # Already explored
    if (i,j,direction) in history:
        return 9999999
    
    history.add((i,j,direction))
    
    available = []

    # Directions
    if direction == 'right':
        if valid(i-1,j):
            available.append(M(i-1,j, 'up'))
        if valid(i+1,j):
            available.append(M(i+1,j, 'down'))          

        if valid(i-1,j+1):
            available.append(val(i,j+1)+M(i-1,j+1, 'up'))
        if valid(i+1,j+1):
            available.append(val(i,j+1)+M(i+1,j+1, 'down'))
        
        if valid(i-1,j+2):
            available.append(val(i,j+1)+val(i,j+2)+ M(i-1,j+2, 'up'))
        if valid(i+1,j+2):
            available.append(val(i,j+1)+val(i,j+2)+ M(i+1,j+2, 'down'))

    if direction == 'left':
        if valid(i-1,j):
            available.append(M(i-1,j, 'up'))
        if valid(i+1,j):
            available.append(M(i+1,j, 'down'))

        if valid(i-1,j-1):
            available.append(val(i,j-1)+M(i-1,j-1, 'up'))
        if valid(i+1,j-1):
            available.append(val(i,j-1)+M(i+1,j-1, 'down'))
        
        if valid(i-1,j-2):
            available.append(val(i,j-1)+val(i,j-2)+ M(i-1,j-2, 'up'))
        if valid(i+1,j-2):
            available.append(val(i,j-1)+val(i,j-2)+ M(i+1,j-2, 'down'))

    if direction == 'up':   
        if valid(i,j-1):
            available.append(M(i,j-1, 'left'))
        if valid(i,j+1):
            available.append(M(i,j+1, 'right'))

        if valid(i-1,j-1):
            available.append(val(i-1,j)+M(i-1,j-1, 'left'))
        if valid(i-1,j+1):
            available.append(val(i-1,j)+M(i-1,j+1, 'right'))
        
        if valid(i-2,j-1):
            available.append(val(i-1,j)+val(i-2,j)+ M(i-2,j-1, 'left'))
        if valid(i-2,j+1):
            available.append(val(i-1,j)+val(i-2,j)+ M(i-2,j+1, 'right'))

    if direction == 'down':
        if valid(i,j-1):
            available.append(M(i,j-1, 'left'))
        if valid(i,j+1):
            available.append(M(i,j+1, 'right'))

        if valid(i+1,j-1):
            available.append(val(i+1,j)+M(i+1,j-1, 'left'))
        if valid(i+1,j+1):
            available.append(val(i+1,j)+M(i+1,j+1, 'right'))
        
        if valid(i+2,j-1):
            available.append(val(i+1,j)+val(i+2,j)+ M(i+2,j-1, 'left'))
        if valid(i+2,j+1):
            available.append(val(i+1,j)+val(i+2,j)+ M(i+2,j+1, 'right'))

    # Dead ends, assume it to be infinity
    if len(available) == 0:
        return 9999999
    
    res = (val(i,j) + min(available))
    memo[(i,j,direction)] = res
    return (res)



print(M(0,0,'right') - val(0,0))