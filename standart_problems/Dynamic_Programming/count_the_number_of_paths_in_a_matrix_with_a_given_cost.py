# given a M x N integer matrix where each cell has a non-negative cost associated 
# with it, count the number of paths to reach the last cell [M][N] from its first cell [0][0]
#such that each path has a given cost. We can only move down or right e.g. (i, j+1) or (i + 1, j)

#Recursive Approach

def count_paths_recursive(matrix, m, n, cost):

    # Base Case, the recusrion stops one the increment in the path is beyond cost
    if cost < 0:
        return 0
    # if we are in the postions (0, 1), (1, 0) or (1, 1)
    if m == 0 and n == 0:
        return 1 if (matrix[0][0]== cost) else 0
    

        # If we are in any posiiton (0, j), it is possible to go left
    if m == 0:
        return count_paths_recursive(matrix, 0, n - 1, cost - matrix[m][n])
    
    # if we are in any position (i, 0) it is possible only to go up
    if n == 0:
        return count_paths_recursive(matrix, m - 1, 0, cost - matrix[m][n])
    
    return count_paths_recursive(matrix, m - 1, n, cost - matrix[m][n]) + count_paths_recursive(matrix, m, n - 1, cost - matrix[m][n])
    
# Another Recursive version 
def count_paths_rec(matrix, m, n, cost):

    if n == 0 and m == 0:
        return 1 if (cost == matrix[0][0]) else 0
    
    if cost < 0:
        return 0
    
    if n < 0 or m < 0:
        return 0
    
    return count_paths_rec(matrix, m-1, n, cost - matrix[m][n]) + count_paths_rec(matrix, m, n -1 , cost - matrix[m][n])



# Dynamic Progrmming Approach
# Time: O(N x M x Cost)
# Space: O(N x M x Cost)

def count_paths_dynamic(matrix, m, n, cost, saved_paths):

    if cost < 0:
        return 0
    if (m == 0) and (n == 0):
        return 1 if (cost == matrix[0][0]) else 0
    key = (m, n, cost)

    if key not in saved_paths:

        if m == 0:
            return count_paths_dynamic(matrix, m, n - 1, cost - matrix[m][n], saved_paths)
        
        elif n == 0:
            return count_paths_dynamic(matrix, m - 1, n, cost - matrix[m][n], saved_paths)
        
        else:
            saved_paths[key] = count_paths_dynamic(matrix, m-1, n, cost - matrix[m][n], saved_paths) + cost_paths_dynamic(matrix, m, n -1, cost - matrix[m][n], saved_paths)
    
    return saved_paths[key]


if __name__ == "__main__":

    matrix = [[4, 7, 1, 6], [5, 7, 3, 9], [3, 2, 1, 2],[7, 1, 6, 3]]
    cost = 25


    count_paths_recursive(matrix, len(matrix)-1, len(matrix[0])-1, cost)

    count_paths_rec(matrix, len(matrix)-1, len(matrix[0])-1, cost)
    
    count_paths_dynamic(matrix, len(matrix)-1, len(matrix[0])-1, cost, saved_paths={})