import copy
from math import prod

with open ('input.txt', 'r') as file:
    lines = file.read().split('\n\n')

rules = lines[0].split('\n')
data = lines[1].split('\n')

codedict = {}
letters = {value:key for (key,value) in enumerate(['x','m','a','s'])}

for rule in rules:
    code = rule.split('{')[0]
    codedict[code] = rule[len(code)+1:-1:]



allpair = [[x for x in range(1,4001)] for _ in range(4)]
accepted = 0

store = [('in', allpair)]



# Process the store dict
while len(store) != 0:

    # Dequeue the first item
    code, numbers = store[0][0], store[0][1]
    
    # Remove the current key
    store = store[1::]

    # Process A, R
    if code == 'A':
        # COUNT THE PRODUCT OF EACH GROUP SEPARATELY AND ADD THEM TO ACCEPTED
        product = 1
        for item in numbers:
            print(len(item))
            product *= len(item)
        accepted += product
        continue
    if code == 'R':
        continue


    # Process the removed key 'code'
    rule = codedict[code].split(',')

    # Processing each smallrule x>2000:px
    filtered_numbers = copy.deepcopy(numbers)
    
    for smallrule in rule:

        # Last one
        if ':' not in smallrule:

            store.append((smallrule, copy.deepcopy(filtered_numbers)))
          

        # Other rules
        else:
            
            cond = smallrule.split(':')[0]
            dest = smallrule.split(':')[1]

            if '<' in cond:
                index = letters[cond.split('<')[0]]
                number = int(cond.split('<')[1])

                # Remove irrelavant numbers for that index
                tmp = copy.deepcopy(filtered_numbers)
                tmp[index] = [x for x in filtered_numbers[index] if x < number]

                store.append((dest, tmp))

                # Update filtered numbers to the next one
                tmp2 = copy.deepcopy(filtered_numbers)
                tmp2[index] = [x for x in filtered_numbers[index] if x >= number]

                filtered_numbers = tmp2


            elif '>' in cond:
                index = letters[cond.split('>')[0]]
                number = int(cond.split('>')[1])

                # Remove irrelavant numbers for that index
                tmp = copy.deepcopy(filtered_numbers)
                tmp[index] = [x for x in filtered_numbers[index] if x > number]

                store.append((dest, tmp))

                # Update filtered numbers to the next one
                tmp2 = copy.deepcopy(filtered_numbers)
                tmp2[index] = [x for x in filtered_numbers[index] if x <= number]

                filtered_numbers = tmp2


print(accepted)