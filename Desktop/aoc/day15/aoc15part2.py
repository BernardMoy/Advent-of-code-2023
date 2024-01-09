with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
# length of lines = 2
    
# Hash function
def hash(str):
    current = 0

    for char in str:
        current += ord(char)
        current *= 17
        current = current % 256

    return current

# Dict in Dict
boxes = {}

for line in lines:
    for str in line.split(','):
        # op -
        if str[-1] == '-':
            op = str[0:len(str)-1]

            # For the relavant box, remove it
            index = hash(op)
            if index in boxes:
                if op in boxes[index]:
                    boxes[index].pop(op)
                    # Pop if the dict becomes empty
                    if len(boxes[index]) == 0:
                        boxes.pop(index)

        # op = num
        else:
            op = str.split('=')[0]
            num = str.split('=')[1]

            index = hash(op)
            if index in boxes:
                boxes[index][op] = num

            else:
                # Create dict
                boxes[index] = {op:num}

print(boxes)

sum = 0

for key, value in boxes.items():
    keylist = list(value.keys())
    valuelist = list(value.values())

    for i in range(len(keylist)):
        sum += int(key+1)*int(i+1)*int(valuelist[i])

print(sum)


