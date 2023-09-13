# Given a target sum, find the total ways to achieve
# that sum with n throws of dice throws with k faces


# Recursive Approach
def dice_throws_recursive(n, k, target_sum, tmp=[]):
    
    if ( n == 0):
        if (target_sum == 0):
            print(tmp[:])
            return 1
        else:
            return 0
    # checks the case when the target sum is oversteped, or target sum is smaller than n
    # so it will need less throws to reach it. It also checks the case when the sum is unreachable
    if (target_sum < 0) or (target_sum < n) or (k*n < target_sum):
        return 0
    
    solution = 0

    for i in range(1, k+1):
        solution += dice_throws_recursive(n - 1, k, target_sum -i, tmp+[i])
    
    return solution

# Dynamic Programming Approach

def dice_throws_dynamic(n, k, target_sum, saved_paths ={}):
    

    if ( n == 0):
        if (target_sum == 0):
            return 1
        else:
            return 0
    # checks the case when the target sum is oversteped, or target sum is smaller than n
    # so it will need less throws to reach it. It also checks the case when the sum is unreachable
    if (target_sum < 0) or (target_sum < n) or (k*n < target_sum):
        return 0
    
    key = (target_sum, n)

    if key not in saved_paths:
        solution = 0
        for i in range(1, k+1):

            solution+= dice_throws_dynamic(n - 1, k, target_sum -i,saved_paths)
            saved_paths[key] = solution
    
    return saved_paths[key]


if __name__ == "__main__":

    dice_throws_recursive(n=2, k=6, target_sum=10)
    
    dice_throws_dynamic(n=2, k=6, target_sum=10)