#Given a maze in form of a binary matrix, find the shortest path's length
# in the maze from a given source to a given destination. The path can only be 
#constructed out of cells having value 1, and at any moment, we can only move
# one step in one of the four direcitons.

# Separate the solution in 3 function, one Bool function will check if it is save to 
# go in a certain cell by using another matrix that will save the visited cells,check if 
# we are operating in the boundaries of the matrix and check if the value at that particular
# point is 1. Another function will take the result of the Bool function and will
# initiate recoursion in than direction (up, down, left, right). Third function will initialize
# the visited matrix and will receive the final result

#Bool function
def isSafe(matrix, visited, x, y):
    return (0 <= x < len(matrix) and 0 <=y < len(matrix[0])) and not (matrix[x][y] == 0 or visited[x][y])

def find_shortest_path_in_maze(matrix, visited, i, j,destination,  min_distance=float("inf"), distance=0):

    if (i,j) == destination:
        return min(min_distance, distance)
    
    visited[i][j] = 1

    # Move Down
    if isSafe(matrix, visited, i + 1, j):
        min_distance = find_shortest_path_in_maze(matrix, visited, i + 1, j, destination, min_distance, distance + 1)

    #Move Right
    if isSafe(matrix, visited, i, j + 1):
        min_distance = find_shortest_path_in_maze(matrix, visited, i, j + 1, destination, min_distance, distance + 1)
    
    #Move Up
    if isSafe(matrix, visited, i - 1, j):
        min_distance = find_shortest_path_in_maze(matrix, visited, i - 1, j, destination, min_distance, distance + 1)
    
    #Move Left
    if isSafe(matrix, visited, i, j - 1):
        min_distance  = find_shortest_path_in_maze(matrix, visited, i, j - 1, destination, min_distance, distance + 1)
    
    visited[i][j] = 0

    return min_distance

def find_shortest_path_length(matrix, source, destination):

    # get the source coordinates
    (i, j) = source

    #Get the destinaition coordinates
    (x, y) = destination

    #Base Case
    if not matrix or len(matrix)== 0 or matrix[i][j] == 0 or matrix[x][y] == 0:
        return -1 
    
    # construct the visited matrix
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    min_distance = find_shortest_path_in_maze(matrix, visited, i, j, destination)

    
    return min_distance #if min_distance != float("inf") else -1

if __name__ == "__main__":

    matrix = [  [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 0, 1, 0, 1], 
                [0, 0, 1, 0, 1, 1, 1, 0, 0, 1], 
                [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
           ]

    source = (0, 0)
    destination = (2, 2)
    destination = (7, 5)

    find_shortest_path_length(matrix, source, destination)
    


 