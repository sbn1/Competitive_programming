# The Shortest Common Supersequence (SCS) is finding the 
#shortest supersequence Z given sequences X and Y such that both X and Y are subsequences of Z.


# Recursive Approach
def SCS(x, y,n,m):
    if n==0 or m==0:
        return n+m
    if x[n-1] == y[m-1]:
        return SCS(x, y, n-1, m-1) + 1
    
    return min(SCS(x, y, n-1, m)+1, SCS(x, y, n, m-1)+1)


#Dynamic Programming Approach

def SCS_dynamic(x, y):

    DP=[[0 for i in range(len(y)+1)] for j in range(len(x)+1)]

    for i in range(len(x)+1):
        DP[i][0] = i
    for j in range(len(y)+1):
        DP[0][j] = j

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1] == y[j - 1]:
                DP[i][j] = DP[i - 1][j - 1]+1
            else:
                DP[i][j] = min(DP[i][j-1]+1, DP[i-1][j]+1)
    return DP[-1][-1]


if __name__=="__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    SCS(X, Y,len(X), len(Y))
    SCS_dynamic(X, Y)