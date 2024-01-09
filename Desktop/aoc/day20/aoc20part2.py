from math import lcm

with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

destdict = {}   # Code : Destination
statedict = {}  # Code : T (high) / F (low)
condict = {}  # Code it listens to : T (high) / F (low)

def reset():

    destdict.clear()   # Code : Destination
    statedict.clear()  # Code : T (high) / F (low)
    condict.clear()  # Code it listens to : T (high) / F (low)

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

# The button function is now used to find the cycles
def button(code):
    queue = [('broadcaster', False)]

    # Process the queue
    while len(queue) != 0:
        # Dequeue
        current = queue[0]
        queue = queue[1::]
        
        current_code = current[0]
        current_state = current[1]

        if current_code == code and current_state:
            return True

        # EVERY destination code counts.
        for destination_code in destdict[current_code]:

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

    return False



reset()



# Assume there is one single & code leading to rx.
# Find it.
prev = [key for key, value in destdict.items() if value == ['rx']][0]

print(condict[prev])

# Find the cycles required for them to turn up H individually.
# All of them must be H for a low pulse to be directed to zr (and then to rx)

cycle_list = []

for i in range(len(condict[prev])):
    count = 0
    reset()
    while not button(condict[prev][i]):
        count += 1
    
    count += 1  # Count the last button press when it exit loop

    cycle_list.append(count)
    print(cycle_list)

print(cycle_list)

print(lcm(*cycle_list))
