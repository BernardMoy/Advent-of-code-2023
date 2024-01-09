with open('aoc12.txt', 'r') as file:
    lines = file.read().split('\n')

def count(string, num):
    output = 0

    # Base cases
    # Empty string
    if len(string) == 0:
        return 1 if len(num) == 0 else 0 
    # Empty num
    if len(num) == 0:
        return 0 if '#' in string else 1
    
    # Case when . : Skip over it bc cant change it
    if string[0] in '.?':
        output += count(string[1:], num)
    
    # Case when #: It must form a continuous ### for how long the first num stated it to
    # Followed by a character that is NOT '#' Afterwards.
    if string[0] in '#?':
        # if len = string, then we dont need to care what comes after it because it ends
        if len(string) >= num[0] and all(item in "#?" for item in string[:num[0]]) and (len(string) == num[0] or string[num[0]] != '#'):
            # Remove the substring and also the last char that has checked to not be '#
            output += count(string[num[0]+1:], num[1:])

    # Case when ? : Consider both cases
    return output

sum = 0

for line in lines:
    string = line.split(' ')[0]
    num = [int(x) for x in line.split(' ')[1].split(',')]
    
    sum += count(string, num)

print(sum)
