from collections import defaultdict

graph=defaultdict(list)

def addEdge(u,v):
    graph[u].append(v)

def BFS(s):
    visited = set()
    queue=[]
    queue.append(s)
    visited.add(s)
    while queue:
        s=queue.pop(0)
        print(s,"->",end=" ")
        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                print(visited)

addEdge(0, 1)
addEdge(0, 2)
addEdge(0, 3)
addEdge(1, 0)

addEdge(2, 0)

addEdge(3, 0)
addEdge(3, 4)
addEdge(4, 3)

# addEdge(1,2)
# addEdge(1,3)
# addEdge(2,4)
# addEdge(2,5)
# addEdge(3,1)
# addEdge(3,5)
# addEdge(4,2)
# addEdge(4,5)
# addEdge(4,6)
# addEdge(5,2)
# addEdge(5,3)
# addEdge(5,4)
# addEdge(6,4)
# addEdge(6,5)
print(len(graph))
print(graph)

BFS(0)