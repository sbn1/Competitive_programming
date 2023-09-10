# Given a rod of length n, find the optimal way to cut the rod into
# smaller rods to maximize the product of each of the smaller rod's price.
# Assum that each rod of length i has price i.

# Recursive Approach

def rod_cutting_recursive(rod_length, n):
    # Base case: if the maximum length of the rod-> n is oversteped
    if rod_length < 0:
        return 0
    # Base case: no items left or the length of the rod is reached
    if n <=0 or rod_length == 0:
        return 1
    # exclude the current element and recur to the reminding ones
    exclude = rod_cutting_recursive(rod_length, n-1)
    # recurence to the same element is allowed, to have 1 X 1 X 1 etc.
    include = rod_cutting_recursive(rod_length - n, n)*n

    return max(exclude, include)

#Dynamic Approach
# Time: O(N**2)
# Space: O(N)
def rod_cutting_dynamic(rod_length):
    # DP[i] stores the maximum profic achieved by the rod of length i 
    DP = [i for i in range(rod_length + 1)]
    # considers the rod has length i
    for i in range(1, rod_length+1):
        # divided the rod of length i into two rods lengths: j and i-j and takes maximum of them
        for j in range(1,i+1):

            DP[i] = max(DP[i], DP[i - j]*j)

    return DP[-1]


if __name__ == "__main__":

    n = 4
    n = 8
    n = 15

    rod_cutting_recursive(n, n)
    rod_cutting_dynamic(n)
