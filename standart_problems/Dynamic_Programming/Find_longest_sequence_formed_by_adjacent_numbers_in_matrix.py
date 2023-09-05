# Given a N x N matrix, with distinctive values. Find the longest 
#sequence formed by adjacent numbers in the matrix such that for each
#number, the number of the adjacent neighbors is +1 its value

# Recursive Approach

# The function will start the search only from a certain point
def find_longest_adjacent(matrix, i, j):
    if not (0 <= i < len(matrix) and 0<=j<len(matrix[0])):
        return []

    path =[]

    #Down movement
    if i > 0 and matrix[i-1][j] == matrix[i][j] + 1:
        path = find_longest_adjacent(matrix, i-1, j)
    
    #Up movement
    if ( i+1 <len(matrix)) and (matrix[i+1])[j] == matrix[i][j] + 1:
        path = find_longest_adjacent(matrix, i+1, j)
    
    #Left movement
    if (j + 1 < len(matrix[0])) and (matrix[i][j+1] == matrix[i][j] + 1):
        path = find_longest_adjacent(matrix, i, j+1)
    
    #Righ movement
    if (j> 0) and (matrix[i][j-1] == matrix[i][j] + 1):
        path = find_longest_adjacent(matrix, i, j - 1)
    
    path.append(matrix[i][j])

    return path

def longest_path(matrix):
    if not matrix or not len(matrix):
        return 0
    
    longestPath = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            path_from_certain_point = find_longest_adjacent(matrix, i, j)
            longestPath = max(longestPath, path_from_certain_point, key=len)
    return longestPath

# Dynamic Programming Approach 
# Time: O(N x N)
# Space: O(N x N)

def find_longest_adjacent_dynamic(matrix, i, j, stored_positions):
    if not (0 <= i < len(matrix) and 0<=j<len(matrix[0])):
        return None

    key = (i, j)

    if key not in stored_positions:
            
        path = None

        #Down movement
        if i > 0 and matrix[i-1][j] == matrix[i][j] + 1:
            path = find_longest_adjacent_dynamic(matrix, i-1, j, stored_positions)
        
        #Up movement
        if ( i+1 <len(matrix)) and (matrix[i+1])[j] == matrix[i][j] + 1:
            path = find_longest_adjacent_dynamic(matrix, i+1, j, stored_positions)
        
        #Left movement
        if (j + 1 < len(matrix[0])) and (matrix[i][j+1] == matrix[i][j] + 1):
            path = find_longest_adjacent_dynamic(matrix, i, j+1, stored_positions)
        
        #Righ movement
        if (j > 0) and (matrix[i][j-1] == matrix[i][j] + 1):
            path = find_longest_adjacent_dynamic(matrix, i, j - 1, stored_positions)
        #storing the elements and putting a comma between them, to keep track of the length
        stored_positions[key] = str(matrix[i][j])+"," +str(path) if path else str(matrix[i][j])

    return stored_positions[key]

def longest_path_dynamic(matrix):
    if not matrix or not len(matrix):
        return 0
    # the dict will store the solutions of the subproblems
    stored_positions = {}

    longest_sequence = float("-inf")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            path_from_certain_point = find_longest_adjacent_dynamic(matrix, i, j, stored_positions)

            #cunt the nr of commas to determine the nr of elements in a sequence
            sequence_legth = path_from_certain_point.count(",")

            if sequence_legth > longest_sequence:
                solution = path_from_certain_point
                longest_sequence = sequence_legth
    

    return solution


if __name__ == "__main__":

    matrix = [[10, 13, 14, 21, 23], 
              [11, 9, 22, 2, 3],
              [12, 8, 1, 5, 4], 
              [15, 24, 7, 6, 20], 
              [16, 17, 18, 19, 25]
              ]
longest_path(matrix)

longest_path_dynamic(matrix)


