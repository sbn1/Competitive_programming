# The longest palindromic sequence in a string

# The same approach like in the Longest common sequence, but with the
#reversed string

#Time: O(N**2)
#Space: O(N**2)


#Backtracking approach, generating all the possible solution
#Time: O(2**N)

def longest_palindromic_sequence_backtracking(x, i, j):
    
    if i > j:
        return 0

    if i == j:
        return 1

    if x[i] == x[j]:
        return longest_palindromic_sequence_backtracking(x, i+1, j - 1) + 2

    return max(longest_palindromic_sequence_backtracking(x, i+1, j), longest_palindromic_sequence_backtracking(x, i, j-1)) 

# Dynamic programming approach
def longest_palindromic_sequence(x):
    y = x[::-1]
    n = len(x)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

if __name__ =="__main__":
    x = "ABBDCACB"
    longest_palindromic_sequence_backtracking(x, 0, len(x)-1)
    longest_palindromic_sequence(x)