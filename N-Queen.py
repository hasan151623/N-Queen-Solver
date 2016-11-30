import random
import math
import sys

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
total_conflict=0
min_conflict=50
iter_count=0
def hillClimbing(state,n):
    max_step=1000000
    count=1
    i=0
    
    while i<max_step:
        neighbors=succesor(state,n)
        current_conflict=conflict(state,n)

        neighbor=bestSuccessor(state,neighbors,n)

        if current_conflict<conflict(neighbor,n):
            #print(count)
            global total_conflict
            total_conflict+=current_conflict
            global min_conflict
            if min_conflict>current_conflict:
                min_conflict=current_conflict
            global iter_count
            iter_count+=count
            #print("IN",count)
            return state
        else:
            state=neighbor
            
        i+=1
        count+=1
   
    iter_count=+count
    total_conflict+=current_conflict
    return state
    
total_conflict_sa=0
min_conflict_sa=50
iter_count_sa=0
def simulatedAnnealing(state,n):
    miu_t=0.1
    T=100
    count=1
    best_conflict=50
    global min_conflict_sa
    min_conflict_sa=conflict(state,n)
    best=[]
    global total_conflict_sa
    global iter_count_sa
    for i in range(1,50000):

        current_conflict=conflict(state,n)
        
        if (T==0 or current_conflict==0):
            if min_conflict_sa> current_conflict:
                min_conflct_sa=current_conflict
            
            total_conflict_sa += current_conflict
            iter_count_sa+=count
            #print("count",count)
            return state
        
        next=randomSuccessor(state,n)
        
        delta_E=conflict(next,n)-current_conflict
        
        if delta_E>0:
            state=list(next)
            if best_conflict>current_conflict:
                best=list(state)

        else:
            possibility=min(1,math.exp(delta_E/T))
            if random.random()<=possibility:
                state=list(next)
                if best_conflict>current_conflict:
                    best=list(state)
        T=T-miu_t
        
        best_conflict=conflict(best,n)
        count+=1
        
    #print("best",count)
    iter_count_sa+=count
    total_conflict_sa+=current_conflict
    return best

def randomSuccessor(state,n):
    row=random.randint(0,n-1)
    col=random.randint(0,n-1)
    state[row]=col
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
    #sys.stdout=open("nqueen_output.txt", "a")
    n=int(input())
    
    start=randomState(n)
    print(start)
    print(conflict(start,n))
    print(printState(start,n))

    total_conf_sa=0
    total_conf_hc=0
    conflicts_sa=[]
    conflicts_hc=[]
   
    for i in range(10):
        print("<<<<--------Iteration no--------->>>>: ", i+1)
        res1=hillClimbing(start,n)
        res2=simulatedAnnealing(start,n)
        
        conf_hc=conflict(res1,n)
        total_conf_hc+=conf_hc
        conflicts_hc.append(conf_hc)
        
        print("----Hill Climbing-----")  
        print(res1)
        print(conf_hc)
        print(printState(res1,n))
        
        conf_sa=conflict(res2,n)
        total_conf_sa+=conf_sa
        conflicts_sa.append(conf_sa)
        
        print("-----Simulated Annealing-----")
        print(res2)
        print(conf_sa)
        print(printState(res2,n))
        
    print("N: ",n)   
    print("Average Iteration(HC): ",iter_count/10)
    print("Average conflict(HC): ", total_conf_hc/10)
    print("Mininmum Conflict(HC): ", min(conflicts_hc))
    print("Average Iteration(SA) :",iter_count_sa/10)
    print("Average conflict(SA): ",total_conf_sa/10)
    print("Minimum conflict(SA):",min(conflicts_sa))

    #sys.stdout.close()
    
                
