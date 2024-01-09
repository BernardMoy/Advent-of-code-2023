with open ('aoc9.txt', 'r') as file:
    lines = file.read().split('\n')
    

def find_next(seq):
    # New number = sum of last number of all sublists
    sum = 0

    # Check if the seq only contains 0
    while not all(elem == 0 for elem in seq):
        new = []
        for i in range(1, len(seq)):
            new.append(seq[i] - seq[i-1])
        sum += seq[-1]
        
        seq = new
    
    return sum



num = []

for line in lines:
    seq = line.split(' ')
    int_seq = [int(item) for item in seq]
    num.append(find_next(int_seq))

print(sum(num))