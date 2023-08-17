# Given n and k generate the combinations 

#The solution involves the backtracking technique,
# it will use a temporary array tmp, a solution list. Once the solution is 
#satisfied, it is stored in the sol list.
# In this case the solution is satisfied when the lenght of the tmp is k.
# to be used DFS

#Time: 
# Space: 

from typing import List
def combinations(n, tmp:List[int], sol:List[int],k:int, index:int)->List[List[int]]:
    # Base Case
    if k == 0:
        sol.append(tmp[:])
        return

    for i in range(index, n+1):
        combinations(n, tmp+[i], sol, k-1, i+1)
    
    return sol

combinations(4, [], [], 2, 1)
