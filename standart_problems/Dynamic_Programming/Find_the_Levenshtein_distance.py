# The Levenstein distance is a way to quantify how different two strings are from 
# one another by counting the minimum number of operations required to transform 
# one string into the other.
# The operations are insertion, deletion, replacement. Each operation 
# has a unit cost.

# Recursive Approach

def levenstein_recursive(X, Y, m, n):

    if m == 0 or n == 0:
        return m+n
    
    if X[m-1] == Y[n -1]:
        cost = 0
    else:
        cost = 1
    return min(levenstein_recursive(X, Y, m-1, n)+1,
               levenstein_recursive(X, Y, m, n-1)+1,
               levenstein_recursive(X, Y, m - 1, n - 1)+cost
               
               )
#Dynamic Programming Approach
# Time: O(N**2)
# Space: O(N**2)

def levenstein_dynamic(X, Y):

    DP = [[0 for j in range(len(Y)+1)] for i in range(len(X)+1)]
    
    for j in range(1,len(Y)+1):
        DP[0][j] = j

    for i in range(1, len(X)+1):
        DP[i][0] = i
    
    for i in range(1,len(X)+1):
        for j in range(1, len(Y)+1):

            if (X[i-1] == Y[j-1]):
                cost = 0
            else:
                cost = 1

            DP[i][j] = min(DP[i - 1][j]+1, 
                           DP[i][j - 1]+1,
                           DP[i - 1][j - 1] + cost
                           )

    return DP[-1][-1]
if __name__ == "__main__":
    X = "kitten"
    Y = "sitting"
    levenstein_recursive(X, Y, len(X), len(Y))
    levenstein_dynamic(X, Y)