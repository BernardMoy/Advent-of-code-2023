with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

vlen = len(lines)
hlen = len(lines[0])

history = set()
cursors = [(0,-1, 'right')]

while len(cursors) != 0:
    for cursor in cursors:

        cursors.remove(cursor)

        i = cursor[0]
        j = cursor[1]
        direction = cursor[2]


        if direction == 'right' and j<hlen-1:
            if lines[i][j+1] in '.-':
                new_cursor = (i,j+1,'right')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i][j+1] == '\\':
                new_cursor = (i,j+1,'down')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i][j+1] == '|':
                new_cursor1 = (i,j+1,'up')
                if new_cursor1 not in history:
                    history.add(new_cursor1)
                    cursors.append(new_cursor1)
                new_cursor2 = (i,j+1,'down')
                if new_cursor2 not in history:
                    history.add(new_cursor2)
                    cursors.append(new_cursor2)
            if lines[i][j+1] == '/':
                new_cursor = (i,j+1,'up')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)

        if direction == 'left' and j>0:
            if lines[i][j-1] in '.-':
                new_cursor = (i,j-1,'left')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i][j-1] == '\\':
                new_cursor = (i,j-1,'up')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i][j-1] == '|':
                new_cursor1 = (i,j-1,'up')
                if new_cursor1 not in history:
                    history.add(new_cursor1)
                    cursors.append(new_cursor1)
                new_cursor2 = (i,j-1,'down')
                if new_cursor2 not in history:
                    history.add(new_cursor2)
                    cursors.append(new_cursor2)
            if lines[i][j-1] == '/':
                new_cursor = (i,j-1,'down')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)

        if direction == 'up' and i>0:
            if lines[i-1][j] in '.|':
                new_cursor = (i-1,j,'up')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i-1][j] == '\\':
                new_cursor = (i-1,j,'left')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i-1][j] == '-':
                new_cursor1 = (i-1,j,'left')
                if new_cursor1 not in history:
                    history.add(new_cursor1)
                    cursors.append(new_cursor1)
                new_cursor2 = (i-1,j,'right')
                if new_cursor2 not in history:
                    history.add(new_cursor2)
                    cursors.append(new_cursor2)
            if lines[i-1][j] == '/':
                new_cursor = (i-1,j,'right')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)

        if direction == 'down' and i<vlen-1:
            if lines[i+1][j] in '.|':
                new_cursor = (i+1,j,'down')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i+1][j] == '\\':
                new_cursor = (i+1,j,'right')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)
            if lines[i+1][j] == '-':
                new_cursor1 = (i+1,j,'right')
                if new_cursor1 not in history:
                    history.add(new_cursor1)
                    cursors.append(new_cursor1)
                new_cursor2 = (i+1,j,'left')
                if new_cursor2 not in history:
                    history.add(new_cursor2)
                    cursors.append(new_cursor2)
            if lines[i+1][j] == '/':
                new_cursor = (i+1,j,'left')
                if new_cursor not in history:
                    history.add(new_cursor)
                    cursors.append(new_cursor)

# Checking existence in set is faster than list!
energized = set()
for pi,pj,dir in history:
    if (pi,pj) not in energized:
        energized.add((pi,pj))

print(len(energized))  


