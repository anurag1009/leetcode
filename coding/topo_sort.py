from collections import defaultdict

graph=defaultdict(list)

def addEdge(u,v):
    graph[u].append(v)

addEdge(5, 2);
addEdge(5, 0);
addEdge(4, 0);
addEdge(4, 1);
addEdge(2, 3);
addEdge(3, 1);

print(graph)

def topo_sort_util(v,visited,stack):
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            visited.add(i)
            topo_sort_util(i,visited,stack)
    stack.insert(0,v)

def topo_sort():
    visited=set()
    stack=[]
    for v in list(graph):
        if v not in visited:
            topo_sort_util(v,visited,stack)
    print(stack)


topo_sort()


