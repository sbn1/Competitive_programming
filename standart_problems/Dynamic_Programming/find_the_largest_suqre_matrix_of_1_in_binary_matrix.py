# Given a M X N matrix, find the size of the largest matrix of 1's.

# Recursive Approach

def binary_matrix_size(matrix, m, n, max_size=0):

    if n < 0 or m < 0:
        return 0, max_size
    
    left, max_size = binary_matrix_size(matrix, m, n-1, max_size)

    top, max_size = binary_matrix_size(matrix, m-1, n, max_size)

    diagonal, max_size = binary_matrix_size(matrix, m-1, n-1, max_size)

    size = 1 + min(min(left, top), diagonal) if matrix[m][n] else 0

    return size, max(size, max_size)

def binary_matrix_dynamic(matrix):

    #DP = [[1]*len(matrix[0])]*len(matrix)

    DP = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    maximum_size = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # keep the 1's in the i==0 or j==0 positions
            DP[i][j] = matrix[i][j]

            if (i > 0) and (j>0) and matrix[i][j] == 1:
                DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])+1

                maximum_size =  max(DP[i][j], maximum_size)

    return maximum_size


if __name__=="__main__":

    matrix = [[0, 0, 1, 0, 1, 1], 
              [0, 1, 1, 1, 0, 0], 
              [0, 0, 1, 1, 1, 1],
              [1, 1, 0, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1, 1],
              [1, 0, 1, 1, 1, 1], 
              [1, 1, 1, 0, 1, 1]]

    matrix = [[1, 0, 1, 1, 1],
              [0, 1, 0, 1, 1], 
              [0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [0, 1, 1, 1, 0]]
    

    binary_matrix_size(matrix, len(matrix)-1, len(matrix[0])-1)[1]
    binary_matrix_dynamic(matrix)




