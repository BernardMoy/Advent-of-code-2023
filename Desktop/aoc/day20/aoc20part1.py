
with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

destdict = {}   # Code : Destination
statedict = {}  # Code : T (high) / F (low)
condict = {}  # Code it listens to : T (high) / F (low)


for line in lines:
    code = line.split(' -> ')[0]
    dest = line.split(' -> ')[1].split(', ')

    # Add to the general dict
    if code == 'broadcaster':
        destdict[code] = dest
        statedict [code] = False
    else:
        destdict[code[1::]] = dest
        statedict [code[1::]] = False

    # Add to condict
    if code[0] == '&':
        condict [code[1::]] = []


# Fill the condict with items
for key in condict:
    for dkey, dvalue in destdict.items():
        if key in dvalue:
            condict[key].append(dkey)

print(destdict)
print(condict)

def button():
    lowcount = 1
    highcount = 0

    queue = [('broadcaster', False)]

    # Process the queue
    while len(queue) != 0:
        # Dequeue
        current = queue[0]
        queue = queue[1::]
        
        current_code = current[0]
        current_state = current[1]

        # EVERY destination code counts.
        for destination_code in destdict[current_code]:

            if current_state:
                highcount += 1
            else:
                lowcount += 1

            # Process the destinations
            # %
            if destination_code not in condict and destination_code in statedict:
                # If low signal is sent, invert it
                if not current_state:
                    statedict[destination_code] = not statedict[destination_code]

                    queue.append((destination_code, statedict[destination_code]))


            # &
            if destination_code in condict:
                # Check if all the codes it is listening to is high (TRUE)

                if all (statedict[listening] for listening in condict[destination_code]):
                    statedict[destination_code] = False
                    queue.append((destination_code, False))

                else:
                    statedict[destination_code] = True
                    queue.append((destination_code, True))
 

    return (lowcount, highcount)

l = 0
h = 0

for i in range(1000):
    (low, high) = button()
    l += low
    h += high

print((l,h))
print(l*h)