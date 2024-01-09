with open ('aoc6.txt', 'r') as file:
    lines = file.read().split('\n')
    times = lines[0][9::].strip().split(' ')
    distances = lines[1][9::].strip().split(' ')
    # Filter out empty spaces
    new_times = [item for item in times if item != '']
    new_distances = [item for item in distances if item != '']

# Given a time and distance, determine the number of possible ways to beat that distance
def func(time, distance):

    count = 0

    # First and last is 0
    for i in range(time):
        if (time-i)*i > distance:
            count+=1

    return count

total = 1

# Match time with distances
for i in range(int(len(new_times))):

    total *= func(int(new_times[i]), int(new_distances[i]))

print(total)

