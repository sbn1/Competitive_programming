# Given an unlimited amount of coins of given denominations, find the minimum
# number of coins required to get the desired change.


# Recursive approach

def coin_change_recursive(coins, n, target):
    # base case: if exact target amount is obtained it stops!
    if target == 0:
        return 0
    # base case: if the target amount is exceeded or target amount is exceeded 
    if n < 0 or target < 0:
        return float("inf")

    # iterate through all possible amount form 0 to n-1, n.
    excluded = coin_change_recursive(coins, n - 1, target)
    included = coin_change_recursive(coins, n, target - coins[n]) + 1

    return min(excluded, included)

# Dynamic Programming Approach
# Time: O(N**2)
# Space: O(N)
def coin_change_dynamic(coins, target):
    # store the minimum nr of coins needed to get an amount of i
    DP = [target+1 for _ in range(target + 1)]
    DP[0] = 0

    for i in range(1, target + 1):

        for c in coins:

            if (i - c >=0):
                DP[i] = min(DP[i], DP[i - c] + 1)
    return DP[target] if DP[target] != target + 1 else -1


if __name__ == "__main__":

    coins = [1, 3, 5, 7]
    target = 15

    coin_change_recursive(coins, len(coins)-1, target)
    coin_change_dynamic(coins, target)
