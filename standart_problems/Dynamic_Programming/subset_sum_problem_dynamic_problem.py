# Given a set of positive integers and an integer target, check if there is
# any non-empty subset that sums to target.

# Example: nums= [7, 3, 2, 5, 8], target = 14
# Output: 14

# Recursive Approach

def subset_sum_recursive(a, n, target):

    if target == 0:
        return True
    
    if (n < 0) or (target < 0):
        return False

    include = subset_sum_recursive(a, n - 1, target - a[n]) 
    exclude = subset_sum_recursive(a, n - 1, target)

    return include or exclude

# Time: O(N x sum(a))
# Space: O(N x sum(a))
def subset_sum_rec_dynamic_prog(a, n, target, saved_paths ={}):

    if target == 0:
        return True
    if (n < 0) or (target < 0):
        return False
    
    key = (n, target)

    if key not in saved_paths:
        include = subset_sum_rec_dynamic_prog(a, n - 1, target - a[n], saved_paths) 
        exclude = subset_sum_rec_dynamic_prog(a, n - 1, target, saved_paths)

        saved_paths[key] = include or exclude

    return saved_paths[key]

# Time: O(N x target)
# Space: O(N x target)
def subset_sum_dynamic_programming(a, target):

    DP = [[False for j in range(target+1)] for i in range(len(a)+1)]

    for i in range(len(a)+1):
        DP[i][0] = True

    for i in range(1, len(a)+1):

        for j in range(1, target+1):

            if a[i-1] > j:
                DP[i][j] = DP[i - 1][j]
            else:
                DP[i][j] = DP[i - 1][j] or DP[i -1 ][j - a[i -1]]

    return DP[-1][-1]

if __name__ == "__main__":

    a = [7,3, 2, 5,8]
    target = 14
    subset_sum_recursive(a,len(a)-1,  target)
    subset_sum_rec_dynamic_prog(a,len(a)-1, target)
    subset_sum_dynamic_programming(a, target)