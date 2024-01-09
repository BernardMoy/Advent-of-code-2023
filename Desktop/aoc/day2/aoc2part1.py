with open ('aoc2.txt', 'r') as file:
    lines = file.read().split("\n")

sumid = 0

# For each line, extract all its numbers of cubes in the format ['1', 'r', '2', 'g']
n = 1

for line in lines:
    violated = False

    sets = line.split(":")[1]
    games = sets.split(";")

    for game in games:
        r = 0
        g = 0
        b = 0
        # Each item represents a num and a col: " 3 blue"
        items = game.split(",")

        for item in items:
            num = int(item.split(" ")[1])  # The number of that cube
            col = item.split(" ")[2][0]  # The first letter of the colour of the cube

            if col == 'r':
                r += num
            if col == 'g':
                g += num
            if col == 'b':
                b += num
        
        # If any draws violates the rule, the entire game has rule violated
        if r>12 or g>13 or b>14:
            violated = True
    
    # Only sum the id if there are no draws that are violated
    if not violated:
        sumid += n

    n+=1

print(sumid)
        
    
