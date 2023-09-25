#Given a positive integer n, print all combinations of numbers between 1 and n having sum n.

# Backtracking 
# Time: Exponential
# Space: exponential

def combinations_sum(n, sol, tmp, suma, index):

    #base case
    if suma>=n:
        if (suma == n):
            sol.append(tmp[:])
        return
    
    for i in range(index, n+1):
        combinations_sum(n, sol, tmp+[i], suma + i, i)
    
    return sol

if __name__ == "__main__":

    combinations_sum(3, [],[],0,1)
    
    combinations_sum(4, [],[],0,1)

    combinations_sum(5, [],[],0,1)

    combinations_sum(6, [],[],0,1)