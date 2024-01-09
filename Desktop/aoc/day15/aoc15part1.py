with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

# Hash function
def hash(str):
    current = 0

    for char in str:
        current += ord(char)
        current *= 17
        current = current % 256

    return current

sum = 0
for line in lines:
    for str in line.split(','):
        sum += hash(str)

print(sum)