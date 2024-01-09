with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

start = (0,[j for j in range(len(lines[0])) if lines[0][j] == '.'][0])

end = (len(lines)-1, [j for j in range(len(lines[-1])) if lines[-1][j] == '.'][0])

print((start, end))

vlen = len(lines)
hlen = len(lines[0])

# Arrows are only in the > and v direction

# Junctions are the nodes in the graph
jctlist = []
for i in range(vlen):
    for j in range(hlen):
        if lines[i][j] in '.>v':
            count = 0
            if i>0 and lines[i-1][j] in '.>v':
                count += 1
            if i<vlen-1 and lines[i+1][j] in '.>v':
                count += 1
            if j>0 and lines[i][j-1] in '.>v':
                count += 1
            if j<hlen-1 and lines[i][j+1] in '.>v':
                count += 1
            # More than 3 openings
            if count >= 3 :
                jctlist.append((i,j))


jctlist = [start] + jctlist
jctlist += [end]
print(jctlist)

# Make it an adjacency list
graph = {}


for jct in jctlist:
    graph[jct] = {}
    # SPread it
    current = [jct]
    visited = []
    count = 0

    while len(current) != 0:
        # Process EVERY ELEMENT OF THE CURRENT ARRAY AT ONCE
        for i in range(len(current)):
            pos = current[0]
            current = current[1::]

            # Junction reached
            if pos in jctlist and count != 0:
                graph[jct][pos] = count
                continue

            # Else
            if pos[0]>0 and lines[pos[0]-1][pos[1]] in '.' and (pos[0]-1,pos[1]) not in visited:
                current.append((pos[0]-1, pos[1]))
            if pos[0]<vlen-1 and lines[pos[0]+1][pos[1]] in '.v' and (pos[0]+1,pos[1]) not in visited:
                current.append((pos[0]+1, pos[1]))
            if pos[1]>0 and lines[pos[0]][pos[1]-1] in '.' and (pos[0],pos[1]-1) not in visited:
                current.append((pos[0], pos[1]-1))
            if pos[1]<hlen-1 and lines[pos[0]][pos[1]+1] in '.>' and (pos[0],pos[1]+1) not in visited:
                current.append((pos[0], pos[1]+1))

            # Mark visited
            visited.append(pos)

        count+=1

print('Graph:')
print(graph)

# Use DFS to find the longest path between the start and end
explored = set()

def dfs(node):
    explored.add(node)

    if node == end:
        return 0
    
    longest_path = 0
    
    for neighbour, weight in graph.get(node, {}).items():
        if neighbour not in explored:
            # Replace the current longest path if longer path found
            longest_path = max(longest_path, dfs(neighbour)+weight)
        # For some reason, the last distance is not considered
        if neighbour == end:
            longest_path += weight

    explored.remove(node)
    return longest_path

print(dfs(start))


            