n = 3







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

def makePaths(lines):
    ret = []
    #for x in range (1,len(lines)+1):
       
    return ret


def isGraph(paths):
    pass

nodes = makeNodes(n)
print(nodes)
lines = makeLines(nodes)
print(lines)
paths = makePaths(lines)
print(paths)
nodes = []
lines = []
paths = []