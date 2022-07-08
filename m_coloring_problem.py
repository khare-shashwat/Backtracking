# inputs
n=int(input())
m=int(input())
e=int(input())
edges=[]
adjMap={}

#creating adjacency list from edges
for i in range(0,e):
    u,v=list(map(int,input().strip().split()))
    edges.append((u,v))
for u,v in edges:
    if(u not in adjMap):
        adjMap[u]={v}
    else:
        adjMap[u].add(v)
    if(v not in adjMap):
        adjMap[v]={u}
    else:
        adjMap[v].add(u)

# func to check for M-coloring condition
def f(node,adjMap,n,m,color):
    if(node==n):
        return True
    for i in range(node,n):
        if(color[i]==0):
            for j in range(1,m+1):
                if(possible(j,color,adjMap,node)):
                    color[i]=j
                    if(f(node+1,adjMap,n,m,color)):
                        return True
                    else:
                        color[i]=0
            return False
    return True

# possible to fill a particular color
def possible(j,color,adjMap,node):
    for neighbor in adjMap[node]:
        if(j==color[neighbor]):
            return False
    return True


# calling m-coloring method f()
color=[0]*n  
if(f(0,adjMap,n,m,color)):
    print(1)
else:
    print(0)

























    
    
    
