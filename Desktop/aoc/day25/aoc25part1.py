import networkx as nx 

with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

G = nx.Graph()


for line in lines:
    source = line.split(': ')[0]
    destset = set(line.split(': ')[1].split(' '))
    # Add an edge between source and dest
    for dest in destset:
        G.add_edge(source, dest)
    # Add the reverse edges
        G.add_edge(dest, source)

print(G)
print(nx.minimum_edge_cut(G))


# Remove the edges
G.remove_edges_from(nx.minimum_edge_cut(G))

print(G)

# Find the connected components
connected_components = list(nx.connected_components(G))

m = 1

for i in connected_components:
    print(len(i))
    m*=len(i)

print(m)



