# Given a set of positive numbers, check if it can be divided into two subsets
# with equal sum

# Recursive Approach

def partition_recursive(a, n, suma):

    if suma == 0:
        return True
    
    if n < 0 or suma < 0:
        return False
    
    include = partition_recursive(a, n - 1, suma - a[n])

    if include:
        return True
    
    exclude = partition_recursive(a, n-1, suma)

    return exclude

def check_partition_recursive(a):

    total_sum = sum(a)
    return partition_recursive(a, len(a)-1, total_sum//2)

# Time: O(N x sum(a))
# Space: O(N x sum(a))

def partition_dynamic(a):
    
    total_sum = sum(a)

    DP = [[False for j in range(total_sum//2 + 1)] for i in range(len(a)+1)]

    for i in range(len(a)+1):
        DP[i][0] = True

    for i in range(1, len(a)+1):

        for j in range(1, total_sum//2 + 1):

            if a[i - 1] > j:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] or DP[i-1][j - a[i-1]]

    return DP[-1][-1]


if __name__ == "__main__":

    a = [3, 1, 1, 2, 2, 1]
    check_partition_recursive(a)
    partition_dynamic(a)
    
