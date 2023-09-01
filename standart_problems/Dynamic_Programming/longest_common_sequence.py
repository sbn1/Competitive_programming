# Given two sequences, find the longest common sequence
#present in both sequences in the same order.

# Time: O(N)
#Space: O(N*N)


# Backtrcking solution
#Time: O(2^(m+n))
def longest_common_sequence_backtracking(x, y, n, m):

    if n==0 or m == 0:
        return 0
    
    if x[n-1] == y[m-1]:
        return longest_common_sequence_backtracking(x,y,n-1,m-1) + 1
    
    return max(longest_common_sequence_backtracking(x,y,n-1,m), longest_common_sequence_backtracking(x,y,n,m-1))

# Dynamic Programming Solution
# Time: O(N*M)
# Space: O(N*M)

def longest_common_sequence_dp(x, y):
    
    n = len(x)
    m = len(y)

    dp = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, m+1):
            if (x[i-1] == y[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

#Time: O(N*M)
#Space: O(min(N,M))

def longest_common_sequence_optimized(x, y):

    if len(x)>len(y):
        n, m = len(x), len(y)
    else:
        m, n = len(x), len(y)
    
    current =[0]*(m + 1) 

    for i in range(n+1):
        previous = current[0]
        for j in range(m+1):
            backup = current[j]

            if (i == 0) or (j == 0):
                continue
            else:
                if (x[i-1] == y[j-1]):
                    current[j] = previous + 1
                else:

                    current[j] = max(current[j-1], current[j])

            previous = backup
    return current[-1]
    
if __name__ == "__main__":

    x = "ABCBDAB"
    y = "BDCABA"
    longest_common_sequence_backtracking(x, y, len(x), len(y))
    longest_common_sequence_dp(x, y)
    longest_common_sequence_optimized(x,y)



