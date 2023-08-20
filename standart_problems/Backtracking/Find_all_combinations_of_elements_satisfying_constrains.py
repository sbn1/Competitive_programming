# Given a positive number n, find all combinations of 2 x n elements such that every
#element from 1 to n appears exactly twice and the distance between its two appearences
# is exactly equal to the value of the element

# Create an array of size 2xn with some default values. Then find all the possibile posiiton for 
# certain element e.g. A[i] and A[i+x+1] should be empty and should exist.
# The recursion will backtrack for all the elements up to n

def find_combinations(a, n,x, sol=[]):

    if x>n:
        sol.append(a[:])
        return
    
    for i in range(2*n):

        if (a[i] == -1) and ((i + x + 1) < 2*n) and (a[i + x + 1] == -1):
            a[i] = x
            a[i+x+1] = x
            find_combinations(a, n, x + 1, sol)
            a[i] = -1
            a[i + x+ 1] = -1
        
    return sol

n =4

find_combinations(a = [-1]*(2*n), n=n, x=1)
