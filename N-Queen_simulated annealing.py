import random
import math

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
            print("count",count)
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
        
    print("best",count)
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
    n=int(input())
    start=randomState(n)
    sa=[]
    #start=[8, 7, 8, 4, 7, 1, 1, 7, 6]
    for i in range(10):
        
        #print(start)
        #print(conflict(start,n))
        #print(printState(start,n))
        res=simulatedAnnealing(start,n)
        sa.append(min_conflict_sa)
        #print(res)
        #print(conflict(res,n))
        #print(printState(res,n))
        #print("total conflict",total_conflict_sa)
        #print("min conflict",min_conflict_sa)
        #print("Total iteration: ",iter_count_sa)
        
    print("Average Iteration :",iter_count_sa/10)
    print("Average conflict: ",total_conflict_sa/10)
    print("Minimum conflict:",min(sa))
