with open ('input.txt', 'r') as file:
    areas = file.read().split('\n\n')



# Return the vertical and horizontal reflections
def reflection_vert (area):

    vlen = len(area)
    hlen = len(area[0])

    # Vertical
    for j in range(hlen):
        violated = False
        
        # Force there to be exactly one set of list that differs by exactly 1.
        difference = 0
        for x in range(j+1):
            
            if  j+x+1 >= hlen or j-x<0:
                continue

            l1 = [area[i][j-x] for i in range(vlen)]
            l2 = [area[i][j+x+1] for i in range(vlen)]
            if l1 == l2 or difference == 0 and diff(l1, l2):
                if diff(l1, l2):
                    difference += 1
                continue
            else:
                violated = True
        
        if not violated and difference == 1:
            return j

    return None
            
def reflection_hori (area):

    vlen = len(area)
 
    # Horizontal
    for j in range(vlen):
        violated = False
        difference = 0
        for x in range(j+1):
            if j+x+1 >= vlen or j-x < 0 or area[j-x] == area[j+x+1]:
                continue
            
            if difference == 0 and diff(area[j-x], area[j+x+1]):
                if diff(area[j-x], area[j+x+1]):
                    difference += 1
                    continue
            else:
                violated = True
        
        if not violated and difference == 1:
            return j
        
    return None

# Determine if two lists differ exactly by 1
def diff(l1, l2):
    diff = 0
    for (i1, i2) in zip(l1, l2):
        if i1 != i2:
            diff += 1
    return diff == 1


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
    if h is not None:
        hlist.append(h+1)
    if v is not None:
        vlist.append(v+1)

print(hlist)
print(vlist)

print(100*sum(hlist) + sum(vlist))