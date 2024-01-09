with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

low_limit = 200000000000000
high_limit = 400000000000000 

# Return the position they collide, return None if not collide.
def collision(x1, y1, sx1, sy1, x2, y2, sx2, sy2):
    # Cal slopes
    m1 = sy1/sx1
    m2 = sy2/sx2

    # Check if they are parallel
    if (m1 == m2):
        
        return None
    

    # Find the position they will collide
    posx = (y2-y1+m1*x1-m2*x2)/(m1-m2)
    posy = m1*posx-m1*x1+y1
    
    # Check if the intersection appears before the time
    if sx1<0 and posx>x1:
        return None 
    if sx1>0 and posx<x1:
        return None 
    if sx2<0 and posx>x2:
        return None 
    if sx2>0 and posx<x2:
        return None 
    
    if sy1<0 and posy>y1:
        return None 
    if sy1>0 and posy<y1:
        return None 
    if sy2<0 and posy>y2:
        return None 
    if sy2>0 and posy<y2:
        return None 
    
    # Check if outside the boundary
    if posx < low_limit or posx > high_limit:
        return None
    if posy < low_limit or posy > high_limit:
        return None 
    
    return (posx, posy)


for i in range(len(lines)):
    coords = lines[i].split(' @ ')[0].split(', ')[0:2]
    speeds = lines[i].split(' @ ')[1].split(', ')[0:2]
    lines[i] = coords + speeds 
    lines[i] = [int(x) for x in lines[i]]


count = 0

for i in range(len(lines)):
    for j in range(i, len(lines)):
        result = collision(*(lines[i]+lines[j]))
        if result:
            count+=1

print(count)



