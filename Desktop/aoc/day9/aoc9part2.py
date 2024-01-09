with open ('aoc9.txt', 'r') as file:
    lines = file.read().split('\n')
    

def find_next(seq):
    # List to store the first number from each sequence
    first = []

    # Check if the seq only contains 0
    while not all(elem == 0 for elem in seq):
        new = []
        for i in range(1, len(seq)):
            new.append(seq[i] - seq[i-1])
        first.append(seq[0])
        
        seq = new
    
    # Navigate the inverted triangle 
    initial = first[-1]
    
    for i in range(-2, -len(first)-1, -1):
        initial = first[i] - initial

    return initial



num = []

for line in lines:
    seq = line.split(' ')
    int_seq = [int(item) for item in seq]
    num.append(find_next(int_seq))

print(num)
print(sum(num))