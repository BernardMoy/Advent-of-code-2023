with open ('input.txt', 'r') as file:
    areas = file.read().split('\n\n')



# Return the vertical and horizontal reflections
def reflection_vert (area):

    vlen = len(area)
    hlen = len(area[0])

    # Vertical
    for j in range(hlen):
        violated = False
        for x in range(j+1):
            if  j+x+1 >= hlen or j-x<0 or all(area[i][j-x] == area[i][j+x+1] for i in range(vlen)):
                continue
            else:
                violated = True
        
        if not violated:
            return j

    return None
            
def reflection_hori (area):

    vlen = len(area)
 
    # Horizontal
    for j in range(vlen):
        violated = False
        for x in range(j+1):
            if j+x+1 >= vlen or j-x < 0 or area[j-x] == area[j+x+1]:
                continue
            else:
                violated = True
        
        if not violated:
            return j
        
    return None


vlist = []
hlist = []

for area in areas:

    area = area.split('\n')
  
    vlen = len(area)
    hlen = len(area[0])

    h = reflection_hori(area)
    v = reflection_vert(area)
    print(h, v)

    # The last row is not counted, otherwise it is reflecting with nothing
    if h != vlen - 1:
        hlist.append(h+1)
    if v != hlen - 1:
        vlist.append(v+1)

print(hlist)
print(vlist)

print(100*sum(hlist) + sum(vlist))