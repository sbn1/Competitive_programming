# Given a M X N integer matrix, find all paths from the first to the last cell. The
# movements can be only down or to the right from the current cell

# Solution: A backtracking approach is to call two recursion, 
#one will move to the rights, the other down. The base cases are set for instances when the
# recursion arrives in the limit of only one dimension, ex. in position a[n][...] or a[...][m] 
#
#Time: O(N+M)
#Space:O(N+M)

from typing import List
def find_all_paths_in_matrix(a:List[List[int]], index_row:int, index_col:int, sol=[], tmp=[])->List[List[int]]:

    if (index_row == len(a)) and (index_col == len(a[0])-1):
        sol.append(tmp[:])
        return
    
    elif (index_row == len(a)) or (index_col == len(a[0])):
        return 
    else:

        find_all_paths_in_matrix(a, index_row+1, index_col, sol, tmp + [a[index_row][index_col]])
        find_all_paths_in_matrix(a, index_row, index_col+1, sol, tmp + [a[index_row][index_col]])
    
    return sol

if __name__ == "__main__":

    find_all_paths_in_matrix([[1,2,3],[4,5,6],[7,8,9]], 0,0)
