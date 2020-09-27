from collections import defaultdict

graph=defaultdict(list)

def addEdge(u,v):
    graph[u].append(v)

def DFS(s):
    visited=set()
    stck=[]
    stck.append(s)
    visited.add(s)
    while stck:
        s=stck.pop()
        print(s,end=" ")
        for i in graph[s]:
            if i not in visited:
                stck.append(i)
                visited.add(i)

#
# addEdge(1, 0);
# addEdge(0, 2);
# addEdge(2, 1);
# addEdge(0, 3);
# addEdge(1, 4);

#traversal answer for this graph: 0->3->2->1->4


addEdge(1,2)
addEdge(1,3)
addEdge(2,4)
addEdge(2,5)
addEdge(3,1)
addEdge(3,5)
addEdge(4,2)
addEdge(4,5)
addEdge(4,6)
addEdge(5,2)
addEdge(5,3)
addEdge(5,4)
addEdge(5,6)
addEdge(6,4)
addEdge(6,5)
print(len(graph))
print(graph)

DFS(1)