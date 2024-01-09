with open ('aoc1.txt', 'r') as file:
    text = file.read()

lines = text.split('\n')

sum = 0
for string in lines:
    nums = []
    
    # extract each number in string
    for i in range(len(string)):
        if string[i].isdigit():
            nums.append(string[i])

    if len(nums) != 0:
        sum += int(nums[0] + nums[-1])

print(sum)

