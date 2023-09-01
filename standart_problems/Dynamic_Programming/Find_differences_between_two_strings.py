# Given two strings, to be found the differences between them.
# If an element is present in the first string, but not in the second, it will have (-) sign
# accordingly it will have (+) if it is present in the second and not in the first

# Example. Y = XMJYAUZ 
#          X = XMJAATZ 
# Output: X M J -Y A -U +A +T Z

# The problem has a similar aproach to longest common sequence
# Check the relationship in the dp matrix between those values that are in Y and not in X, 
# and those that are in X but not in Y

# Time: O(N*M)
#Space: O(N*M)

def find_longest_common_sequence(x, y ):

    n, m = len(x), len(y)

    dp = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if (x[i-1] == y[j - 1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def find_differences_between_string(x, y, n, m, dp):
    
    if (n > 0) and (m > 0) and (x[n-1] == y[m-1]):
        find_differences_between_string(x, y, n-1, m - 1, dp)
        print(" ", x[n-1], end=" ")
    
    elif (m > 0) and (n ==0 or dp[m-1][n] >= dp[m][n-1]):
        find_differences_between_string(x, y, n, m-1, dp)
        print("+", y[m-1], end=" ")
    
    elif (n > 0) and (m ==0 or dp[m-1][n] < dp[m][n-1]):
        find_differences_between_string(x, y, n-1, m, dp)
        print(" - ", x[n-1], end=" ")

if __name__ == "__main__":

    Y = "XMJYAUZ" 
    X = "XMJAAT"
    dp = find_longest_common_sequence(X, Y)

    find_differences_between_string(Y,X,  len(X), len(Y), dp)

