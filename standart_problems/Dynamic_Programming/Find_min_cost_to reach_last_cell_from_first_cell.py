# Given a matrix M x N where each cell has a cost, 
# find the minimum cost to reach the last cell, from the first cell
# From posiiton [0][0] to [n][m]


# Recursive Approach

def min_cost_path(matrix, m,n):
    # Base case
    if (n ==0) and (m ==0):
        return matrix[0][0]
    # Since we  search for the minimum, when crossing over the matrix borders it will cast
    # the higest possible value, so that the min function will ignore thiose paths
    if (m < 0) or (n <0):
        return float("inf")
    
    
    return min(min_cost_path(matrix, m - 1, n), min_cost_path(matrix, m, n - 1)) + matrix[m][n]

# Dynamic Programming Approach 
#Time: O(N**2)
# Space: O(N**2)
def min_cost_path_dynamic(matrix):

    DP_cost = [[float("inf") for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
    DP_cost[1][1] = matrix[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not(i== 0 and j == 0):
                DP_cost[i+1][j+1] = matrix[i][j] + min(DP_cost[i+1][j], DP_cost[i][j+1])
    
    return DP_cost[-1][-1]

if __name__ == "__main__":


    matrix = [[4, 7, 8, 6, 4],
              [6, 7, 3, 9, 2], 
              [3, 8, 1, 2, 4],
              [7, 1, 7, 3, 7],
              [2, 9, 8, 9, 3]
              ]
    
    min_cost_path(matrix, len(matrix)-1, len(matrix[0])-1)

    