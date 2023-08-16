#Given a positive integer n, print all combinations of numbers between 1 and n having sum n.

# Backtracking 

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
    
    n = 5
    combinations_sum(n, [],[],0,1)