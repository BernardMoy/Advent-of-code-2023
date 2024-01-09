with open ('aoc2.txt', 'r') as file:
    lines = file.read().split("\n")

sum = 0

# For each line, extract all its numbers of cubes in the format ['1', 'r', '2', 'g']
n = 1

for line in lines:

    sets = line.split(":")[1]
    games = sets.split(";")

    # Use an array to store all the numbers for that colour to find the maximum
    r = []
    g = []
    b = []

    for game in games:

        # Each item represents a num and a col: " 3 blue"
        items = game.split(",")

        for item in items:
            num = int(item.split(" ")[1])  # The number of that cube
            col = item.split(" ")[2][0]  # The first letter of the colour of the cube

            if col == 'r':
                r.append(num)
            if col == 'g':
                g.append(num)
            if col == 'b':
                b.append(num)
        
    # The max appeared number is the minimum number of cubes of that colour to make the game possible
    sum += max(r)*max(g)*max(b)

print(sum)
        
    
