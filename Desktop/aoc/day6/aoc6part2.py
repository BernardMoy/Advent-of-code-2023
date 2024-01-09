with open ('aoc6.txt', 'r') as file:
    lines = file.read().split('\n')
    times = lines[0][9::].strip().split(' ')
    distances = lines[1][9::].strip().split(' ')
    
    str_time = ""
    str_distance = ""

    # Concat the strings in both arrays
    for item in times:
        if item != '':
            str_time += item
    
    for item in distances:
        if item != '':
            str_distance += item

# Given a time and distance, determine the number of possible ways to beat that distance
def func(time, distance):

    count = 0

    # First and last is 0
    for i in range(time):
        if (time-i)*i > distance:
            count+=1

    return count

total = 1

total *= func(int(str_time), int(str_distance))

print(total)

