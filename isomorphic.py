def makeNodes(n):
    ret = []
    for x in range(0,n):
        ret.append(x)
    return ret

def makeLines(nodes):
    ret = []
    for x in range(0, len(nodes)):
        if(x != (len(nodes)-1)): 
            for y in range(x+1, len(nodes)):
                ret.append(f"{nodes[x]}-{nodes[y]}")
    return ret

def makePaths(lines, n):
    ret = [] #blank = graph with no edges
    lenLines = len(lines)
    for k in range (1,lenLines+1):
        print(f"makePaths: k={k}/{lenLines}")
        __pathsRecurse(lines,"",-1,ret,k-1, False)
    '''
    k = 3
    for x in range(0, len(lines)):
        path = ""
        a = lines[x]
        path = path + f"-{a}"
        for y in range (x+1, len(lines)):
            path = f" {a}"
            b = lines[y]
            path = path + f" {b}"
            for z in range (y+1, len(lines)):
                path = f"{a} {b}"
                c = lines[z]
                path = path + f" {c}"
                ret.append(path)
    '''
    return ret
def __pathsRecurse(lines, path: str, a: int, ret, ttl: int, DEBUG: bool):
    for x in range(a+1, len(lines)):
        if(DEBUG): print(f"x: {x} | a: {a} | ttl: {ttl} | path: {path}")
        if(not ttl <= 0): # If not last element
            __pathsRecurse(lines, (path + f" {lines[x]}"), x, ret, (ttl-1), DEBUG)
        else:
            if(DEBUG): print(f"Killed Thread | path: {(path + f' {lines[x]}')}")
            ret.append((path + f" {lines[x]}"))
          

'''
def __isGraph(path, nodes) -> bool:
    #print(f"Path:  {path} | Nodes:  {nodes}")
    path = path.strip().split(" ")
    #print(f"Path:  {path} | Nodes:  {nodes}")
    foundNodes = []
    __isGraphRecurse(path, nodes, foundNodes, nodes[0], False)
    #print(f"foundNodes:  {foundNodes}")
    if(len(foundNodes) == len(nodes)): return True
    else: return False
def __isGraphRecurse(path: list, nodes: list, foundNodes: list, a: int, DEBUG: bool) -> None:
    active = []
    if(a not in foundNodes): foundNodes.append(a)
    
    if(DEBUG): print("- - - - - - - - - - - - - ")
    #print(f"PRE| path: {path} | nodes: {nodes} | foundNodes: {foundNodes} | a: {a} | active: {active}")
    if(DEBUG): print(f"PRE| foundNodes: {foundNodes} | a: {a} | active: {active}")
    for line in path:
        l = line.split("-")
        if(int(a) == int(l[0])): # Gets target if current node is in a part of the line
            t = int(l[1])
            if(t not in foundNodes): active.append(t)
        elif(int(a) == int(l[1])):
            t = int(l[0])
            if(t not in foundNodes): active.append(t)
        else:
            continue
    
    #print(f"POST| path: {path} | nodes: {nodes} | foundNodes: {foundNodes} | a: {a} | active: {active}")
    if(DEBUG): print(f"POST| foundNodes: {foundNodes} | a: {a} | active: {active}")
    for x in active:
        #if(DEBUG): print(f"a: {a} | t: {t}")
        __isGraphRecurse(path, nodes, foundNodes, x, DEBUG)
def makeGraphs(paths: list, nodes: list):
    ret = []
    pathLength = len(paths)
    for path in range(0, pathLength):
        if(__isGraph(paths[path], nodes)):
            ret.append(paths[path])
            if(path%10000 == 0):
                print(f"makeGraphs: ({path}/{pathLength})")
    return ret
'''   

def findClasses(paths, nodes):
    ret = {}
    for path in paths:
        #print(f"paths: {path}")
        path = path.strip().split(" ")
        comps = {}
        for x in nodes:
            comps.update({str(x): 0})

        
        for line in path: #Splits line into multiple components #Works
            c = line.split("-")
            comps.update({str(c[0]): comps[str(c[0])]+1})
            comps.update({str(c[1]): comps[str(c[1])]+1})

        #print(f"comps:  {comps}")

        values = list(comps.values())
        linesPerNode = [values[0]]
        for x in range(1, len(values)): #Takes number of lines per node and orders greatest to least
            for v in range(0, len(linesPerNode)):
                #print(f"x:{x} | v:{v} | values[x]:{values[x]} | linesPerNode[v]:{linesPerNode[v]} | linesPerNode:{linesPerNode}")
                if(values[x] >= linesPerNode[v]):
                    #print("insert")
                    linesPerNode.insert(v,values[x])
                    break
                #print(f"v: {v} | len: {len(linesPerNode)-1}")
                if(v == len(linesPerNode)-1):
                    #print(f"append")
                    linesPerNode.append(values[x])

                

        #print(f"linesPerNode: {linesPerNode}")

        #continue
        
        if(str(comps) in ret.keys()):
            ret.update({str(linesPerNode): ret[str(linesPerNode)]+1})
        else:
            ret.update({str(linesPerNode): 1})
        #print(f"ret:  {ret}")
        #print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        #break
    return ret

            
f = open("isometricResults.txt", "a")

n=8 #Doesn't work for n=0
lim = 8
while(True):
    print("- - - - - - - - - - - - - - - - - - - - - - -")
    nodes = makeNodes(n)
    print(f"n={n}\n#Nodes: {len(nodes)}")
    lines = makeLines(nodes)
    print(f"#Lines: {len(lines)}")
    paths = makePaths(lines, n)
    print(f"#Paths: {len(paths)}")
    classes = findClasses(paths, nodes)
    print(f"#classes:  {len(list(classes.values()))+1}") # '+1' deals with a graph with no edges




    #graphs = makeGraphs(paths, nodes)
    #print(f"#Graphs: {len(graphs)}")
    f.write(f"n={n} | #Nodes: {len(nodes)} | #Lines: {len(lines)} | #Paths: {len(paths)} | #Classes: {len(list(classes.values()))+1}\n")
    
    if(n==lim):
        break
    n = n+1
f.close()