# The longest common substring problem is the problem of finding 
# the longest string that is a substring of two strings.

#Standart Dynamic programming approach, using memoization

# Time: O(N*M)
#Space: O(N*M)

def longest_commmon_substring(x, y):

    n, m = len(x), len(y)
    max_length = 0
    ending_index = 0

    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if (x[i-1] == y[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1

                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    ending_index = i
    return x[ending_index-max_length:ending_index]

if __name__ =="__main__":


    longest_commmon_substring(x = "ABAB", y = "BABA")
            