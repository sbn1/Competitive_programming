# In the 0-1 knapsack problem, we are given a set of items, each with a specific 
# weight and value. We need to determine the number of each item to include in
# a collection so that the total weight is less or equal than a given limit
#and the total value is as large as possible.

# Recursive Approach

def knapsack_recoursive(values, weights, W, n):
    if W < 0:
        return float("-inf")
    
    if n < 0 or W ==0:
        return 0
    
    exclude = knapsack_recoursive(values, weights, W, n - 1)

    include = values[n] + knapsack_recoursive(values, weights, W - weights[n], n - 1)

    return max(exclude, include)

# Dynamic Programming Approach - Top bottom manner
# Time: O(n x W)
# Space: O(n x W)

def knapsack_dynamic(values, weights, W, n, saved_paths={}):

    if W < 0 :
        return float("-inf")
    
    if n < 0 or W == 0:
        return 0
    
    key = (n, W)
    
    if key not in saved_paths:

        excluded = knapsack_dynamic(values, weights, W, n - 1, saved_paths)
        
        included = values[n] + knapsack_dynamic(values, weights, W - weights[n], n-1, saved_paths)

        saved_paths[key] = max(included, excluded)

    return saved_paths[key]


# Dynamic Approach  - Bottom-up manner
# Time: O(n x W)
# Space: O(n x W)
def knapsack_dynamic_BttmUp(values, weights, W):
    # memoization matrix
    DP = [[0 for i in range(W +1)] for j in range(len(values) + 1)]

    for i in range(1, len(values)+1):

        for j in range(W+1):

            if weights[i -1] > j:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i -1][j - weights[i -1]] + values[i-1])
    return DP[-1][-1]

if __name__ == "__main__":
    values = [20, 5, 10, 40, 15, 25]
    weights = [1, 2, 3, 8, 7, 4]
    W = 10
    knapsack_recoursive(values, weights, W, len(values)-1)
    knapsack_dynamic(values, weights, W,len(values)-1)
    knapsack_dynamic_BttmUp(values, weights, W)