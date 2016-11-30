import random

def conflict(state,n):
    h=0
    for i in range(n):
        for j in range(i+1,n):
            #conflict for same column

            if state[i]==state[j]:
                h+=1
            #conflict for diagonal position
            if abs(i-j)==abs(state[i]-state[j]):
                h+=1
    return h

def succesor(state,n):
    neighbors={}
    for row in range(n):
        for col in range(n):
            if state[row]==col:
                continue
            state_copy=list(state)
            state_copy[row]=col  #move to new column
            neighbors[(row,col)]=conflict(state_copy,n)
    
    return neighbors
    
    


def bestSuccessor(state,neighbors,n):
    
    m=10000
    best_neighbors=[]
    for next_state,next_conflict in neighbors.items():
        if next_conflict < m:
            m=next_conflict
        if m==next_conflict:
                best_neighbors.append(next_state)

    if len(best_neighbors)>0:
        random_next=random.randint(0,len(best_neighbors)-1)
        row,col=best_neighbors[random_next]
        #col=best_neighbors[random_next][1]
        state[row]=col
    return state
    
def hillClimbing(state,n):
    max_step=1000
    count=1
    i=0
    while i<max_step:
        neighbors=succesor(state,n)
        current_conflict=conflict(state,n)

        neighbor=bestSuccessor(state,neighbors,n)

        if current_conflict<=conflict(neighbor,n):
            print(count)
            return state
        else:
            state=neighbor
            
        i+=1
        count+=1
    print(count)
    return state
    
            
        
def randomState(n):
    state=[]
    for row in range(n):
        state.append(random.randint(0,n-1))
    return state

def printState(state,n):
    for i in state:
        for j in range(n):
            if i==j:
                print("Q",end="  ")
            else:
                print("0",end="  ")

        print()

    
if __name__=="__main__":
    n=int(input())
    start=randomState(n)
    #start=[9, 3, 8, 2, 4, 6, 0, 0, 5, 7]
    print(start)
    print(conflict(start,n))
    print(printState(start,n))
    res=hillClimbing(start,n)
    print(res)
    print(conflict(res,n))
    print(printState(res,n))
    
    #print(simulatedAnnealing(start,n))
                
