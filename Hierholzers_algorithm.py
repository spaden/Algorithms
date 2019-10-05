def printCircuit(graph):
    print(graph)
    dct={}
    
    for i in range(len(graph)):
        dct[i]=len(graph[i])
    print(dct)
    if len(graph)==0:
        return
    
    curr_path=[]
    
    circuit=[]
    
    curr_path.append(0)
    curr_v=0
    check = True
    while len(curr_path)!=0:
        print()
        print("current path 1")
        print(curr_path)
        print() 
        
        if check == True:
            curr_path.pop()
            check= False
        
        if dct[curr_v]>0:
            curr_path.append(curr_v)
        
            next_v = graph[curr_v][len(graph[curr_v])-1]
            print("Next Vertex")
            print(next_v)
            print()
            dct[curr_v]-=1
            graph[curr_v].pop(0)
            
            curr_v = next_v
        
        else:
            
            circuit.append(curr_v)
            print("circuit now 1")
            print(circuit)
            print()
            curr_v = curr_path.pop()
            print("curr_path 2")
            print(curr_path)

    print(circuit)
    print(str(0), end=" -> ")
    for i in range(1,len(circuit)+1):
        print(str(circuit[-i]), end=" ->")
graph=[]

graph.append([1])
graph.append([2])
graph.append([0])
printCircuit(graph)