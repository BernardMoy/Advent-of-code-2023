with open ('input.txt', 'r') as file:
    lines = file.read().split('\n\n')

rules = lines[0].split('\n')
data = lines[1].split('\n')

codedict = {}
letters = {value:key for (key,value) in enumerate(['x','m','a','s'])}

for rule in rules:
    code = rule.split('{')[0]
    codedict[code] = rule[len(code)+1:-1:]


# Find the next code to redirect to
def findNext(code, numbers):
    rule = codedict[code].split(',')

    # Processing each smallrule x>2000:px
    for smallrule in rule:
        # Last one
        if ':' not in smallrule:
            return smallrule
        # Others
        cond = smallrule.split(':')[0]
        if '<' in cond:
            index = letters[cond.split('<')[0]]
            number = int(cond.split('<')[1])

            if numbers[index] < number:
                return smallrule.split(':')[1]

        elif '>' in cond:
            index = letters[cond.split('>')[0]]
            number = int(cond.split('>')[1])

            if numbers[index] > number:
                return smallrule.split(':')[1]


# Process data
for i in range(len(data)):
    tmp = data[i].split(',')
    lis = [int(x) for x in [tmp[0][3::], tmp[1][2::], tmp[2][2::], tmp[3][2:-1:]]]
    data[i] = lis

total = 0
for pair in data:
    current = 'in'

    while current != 'A' and current != 'R':
        current = findNext(current, pair)

    if current == 'A':
        total +=sum(pair)

print(total)