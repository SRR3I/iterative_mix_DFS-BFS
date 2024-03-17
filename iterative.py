def DepthFirstSearch(Goal, start, Graph):
    stack, path = [], []
    found = False
    stack.append(start)
    x = start
    while stack:
        stack.pop(0)
        path.append(x)
        if Goal == x:
            found = True
            break
        for c in reversed(Graph[x]):
            stack.insert(0, c)
        if stack:
            x = stack[0]
    return path, found

def IterativeDeepeningSearch(Goal, start, Graph):
    level = {}
    level[start]=[]   
    box = []
    path=[]
    box.append(start)
    found=False
    while box and found==False:
        outdfs=DepthFirstSearch(Goal,start,level)
        found=outdfs[1]
        path=outdfs[0]
        root=box[0]
        level[root] = Graph[root]
        for child in Graph[root]:
            level[child] = []
            box.append(child)
        box.pop(0)
    if found:
        PreviousNode=Goal
        for i in reversed(range(len(path[:-1]))):
            if PreviousNode not in Graph[path[i]]:
                path.pop(i)
            PreviousNode=path[i]
        print("path =",path)
    else:
        print("Not exist!")
        
Graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

IterativeDeepeningSearch('F', 'A', Graph)
