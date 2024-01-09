with open ('aoc7.txt', 'r') as file:
    lines = file.read().split('\n')

keys = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


# Compare two cards if they have the same kind
def same_compare(card1, card2):
    for i in range(5):
        if keys.index(card1[i]) > keys.index(card2[i]):
            return -1
        elif keys.index(card1[i]) < keys.index(card2[i]):
            return 1
        # If equal, process to the next letter
    return 0

# Find the most appeared char, excluding J
def find_max(card):
    count = {}
    for char in card:
        if char == 'J':
            continue

        count[char] = count.get(char, 0) + 1 #Default = 0
    return max(count, key = count.get)

# Find the type of card, with five of a kind = 0
def find_kind(card):

    # For the case JJJJJ
    if card == 'JJJJJ':
        card = '22222'

    # Convert J to the most appeared alphabet
    tmp = list(card)
    for i in range(len(tmp)):
        if tmp[i] == 'J':
            tmp[i] = find_max(card)

    cardlist = tmp
    unique = list(set(cardlist))
    if len(unique) == 1:
        return 0
    elif len(unique) == 2:
        if cardlist.count(unique[0]) == 1 or cardlist.count(unique[0]) == 4:
            return 1
        else:
            return 2
    elif len(unique) == 3:
        if cardlist.count(unique[0]) == 3 or cardlist.count(unique[1]) == 3 or cardlist.count(unique[2]) == 3:
            return 3
        else:
            return 4
    elif len(unique) == 4:
        return 5
    else:
        return 6


# return 1 if card1 is greater than card2, -1 if card2 is greater, 0 otherwise
def compare(card1, card2):
    if find_kind(card1) < find_kind(card2):
        return 1
    elif find_kind(card1) > find_kind(card2):
        return -1
    else:
        return same_compare(card1, card2)

# Dictionary to store (card, num) in their order
dict = []

for line in lines:
    added = False

    card = line.split(" ")[0]
    num = line.split(" ")[1]

    # First card
    if len(dict) == 0:
        dict.append((card, num))
        added = True

    # Other cards
    for i in range(len(dict)):

        if compare(card, dict[i][0]) == -1 and not added:
            dict.insert(i, (card, num))
            added = True

    # It is the weakest
    if not added:
        dict.append((card, num))


print(dict)

total = 0

for i in range(len(dict)):
    total += (i+1)*(int(dict[i][1]))  # Ranking = i+1

print(total)
