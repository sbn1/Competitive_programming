# Given a rod length n and a list of rod prices of length i, whenre 1 <= i <= n, 
# find the optimal way to cut the rod into smaller rods to maximize profit

# Recursive Approach

def rod_cutting_recursive(length, prices, rod_length, n):

    if rod_length <0:
        return float("-inf")
    
    if (n < 0) or (rod_length == 0):
        return 0
    
    # Exclude the current element and recur to the reminding
    exclude = rod_cutting_recursive(length, prices, rod_length, n -1) 
    # recurse the element but from n, not (n-1) since the rod can be divided in many
    #  pieces of the same length
    include = rod_cutting_recursive(length, prices, rod_length - length[n], n) + prices[n]

    return max(exclude, include)

#Dynamic Programming Approach
# Time: O(N**2)
# Space: O(N)
def rod_cutting_dynamic(prices, n):

    DP = [0]*(n + 1)

    for i in range(1, n+1):
        for j in range(1, i+1):

            DP[i] = max(DP[i], DP[i - j] + prices[j - 1])

    return DP[n]

if __name__ == "__main__":

    length = [1, 2, 3, 4, 5, 6, 7, 8]
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rod_length = 4

    rod_cutting_recursive(length, prices, rod_length, len(prices)-1)
    rod_cutting_dynamic(prices, rod_length)