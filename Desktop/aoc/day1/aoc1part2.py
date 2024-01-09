with open ('aoc1.txt', 'r') as file:
    text = file.read()

lines = text.split('\n')

# Given a string, output its number form
def find_number(s):
    number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, word in enumerate(number_words, start = 1):
        if s == word:
            return index
    return None

print(find_number("six"))

sum = 0
for string in lines:
    nums = []
    
    # extract each number in string
    for i in range(len(string)):

        # Check if i is the beginning of a number_word
        # The length of word is between 3 and 5 characters, so we check if the letter and its latter letters correspond to a number
        for word_len in range(3,6):
            if len(string) - i >= word_len and find_number(string[i : i + word_len]):
                nums.append(str(find_number(string[i : i + word_len])))

        # Check if the character itself is a digit
        if string[i].isdigit():
            nums.append(string[i])

    if len(nums) != 0:
        sum += int(nums[0] + nums[-1])

print(sum)

