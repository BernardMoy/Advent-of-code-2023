with open('aoc4.txt', 'r') as file:
    lines = file.read().split('\n')

# A list of all 1s that will be modified later
numbers = []
# The number of winning cards for each line
winning_numbers = []

for line in lines:
    n = 0

    # Get arrays of winning cards and the cards you own
    winning_cards = line.split('|')[0].split(":")[1].split(" ")
    cards = line.split('|')[1][1::].split(" ")

    for i in cards:
        # Ignore the ''s generated by single digit numbers
        if i != '' and i in winning_cards:
            n+=1
    
    # n represents the number of winning cards
    numbers.append(1)
    winning_numbers.append(n)

print(numbers)
print(winning_numbers)

# Modify numbers according to the rules
for i in range(len(numbers)):
    # j = The number of winning cards for that index
    for j in range(i+1, i + winning_numbers[i]+1):
        numbers[j] += numbers[i]  # numbers[i] = the number of cards including duplicate cards

print(numbers)

sum = 0
for i in numbers:
    sum += i

print(sum)