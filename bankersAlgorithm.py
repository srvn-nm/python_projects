# Total number of process
P = 3
 
# Total number of resources
R = 3
  
# Total safe-sequences
total = 0
  
# Function to check if process
# can be allocated or not
def is_available(process_id, allocated,
                 max, need, available):
                      
    flag = True
  
    # Check if all the available resources
    # are less greater than need of process
    for i in range(R):
        if (need[process_id][i] > available[i]):
            flag = False
  
    return flag
 
# Print all the safe-sequences
def safe_sequence(marked, allocated,
                  max, need, available, safe):
     
    global total, P, R
     
    for i in range(P):
         
        # Check if it is not marked
        # already and can be allocated
        if (not marked[i] and
            is_available(i, allocated, max,
                         need, available)):
                              
            # mark the process
            marked[i] = True
  
            # Increase the available
            # by deallocating from process i
            for j in range(R):
                available[j] += allocated[i][j]
  
            safe.append(i)
             
            # Find safe sequence by taking process i
            safe_sequence(marked, allocated, max,
                          need, available, safe)
            safe.pop()
  
            # unmark the process
            marked[i] = False
  
            # Decrease the available
            for j in range(R):
                available[j] -= allocated[i][j]
         
    # If a safe-sequence is found, display it
    if (len(safe) == P):
        total += 1
         
        for i in range(P):
            print("P" + str(safe[i] + 1), end = '')
            
            if (i != (P - 1)):
                print("--> ", end = '')
             
        print()
        
        

def bankers(resources):
  
    # Available vector of size R
    available = [0 for i in range(R)]
     
    for i in range(R):
        sum = 0
         
        for j in range(P):
            sum += allocated[j][i]
  
        available[i] = resources[i] - sum
     
  
    # Safe vector for displaying a
    # safe-sequence
    safe = []
  
    # Marked of size P for marking
    # allocated process
    marked = [False for i in range(P)]
  
    # Need matrix of size P*R
    need = [[0 for j in range(R)]
               for i in range(P)]
     
    for i in range(P):
        for j in range(R):
            need[i][j] = (max[i][j] -
                    allocated[i][j])
     
    if total > 0:
        print("Safe sequences are:")
     
    safe_sequence(marked, allocated, max,
                  need, available, safe)
     
    print("\nThere are total " + str(total) +
          " safe-sequences")
    
    print(resources)
    
    print("---------------------------------------------")
  
# Driver code       
if __name__=="__main__":
     
    # Allocated matrix of size P*R
    allocated = [ [ 1, 0, 1 ],
                  [ 2, 0, 4 ],
                  [ 1, 2, 3 ]]
  
    # max matrix of size P*R
    max = [ [ 2, 2, 2 ],
            [ 2, 0, 5 ],
            [ 3, 4, 4 ]]
  
    for i in range(5):
        for j in range(5):
            for k in range(5):
                bankers([i,j,k])