import copy
import sys
sys.setrecursionlimit(1500)

with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

# Dict to store graph
graph = {}

for line in lines:
    source = line.split(': ')[0]
    destset = set(line.split(': ')[1].split(' '))
    graph[source] = destset


# ADD THE REVERSE EDGES TO THE GRAPH
keys_storage = [key for key in graph.keys()]

for key in keys_storage:
    for item in graph[key]:

        if item in graph.keys():
            graph[item].add(key)
        
        else:
            graph[item] = set()
            graph[item].add(key)


# Function to check if the graph is connected
def isconnected(graph):
    # Check if all vertices can be visited via DFS
    visited = set()

    def dfs(vertex):
        visited.add(vertex)
        if vertex in graph:
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    dfs(neighbour)
    
    start = next(iter(graph.keys()))
    # Fill the visited set with dfs
    dfs(start)
    if not len(visited) == len(graph):
        print(len(visited))
        print(len(graph))
        return False
    return True

# Given a graph and start vertex, calculate the size of group FOR THAT CONNECTED COMPONENT
def calculate_size(graph, start):
    pass

# BRUTE FORCE O(N^6)
def disconnect(graph):
    # Now try to iterate over the graph to disconnect 3 edges.
    original_graph = copy.deepcopy(graph)

    # All reverse edges are already added to the graph.
    for source1 in original_graph.keys():
        for dest1 in original_graph[source1]:

            for source2 in original_graph.keys():
                for dest2 in original_graph[source2]:

                    for source3 in original_graph.keys():
                        for dest3 in original_graph[source3]:

                            graph[source1].discard(dest1)
                            graph[dest1].discard(source1)

                            graph[source2].discard(dest2)
                            graph[dest2].discard(source2)

                            graph[source3].discard(dest3)
                            graph[dest3].discard(source3)

                            if not isconnected(graph):
                                # Restore original graph
                                graph = copy.deepcopy(original_graph)
                                return (source1, dest1, source2, dest2, source3, dest3)
                            
                            graph = copy.deepcopy(original_graph)
    return None 

print(disconnect(graph))

            



