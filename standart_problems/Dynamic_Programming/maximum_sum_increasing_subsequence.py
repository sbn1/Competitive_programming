# Find the subsequence of a give sequence such that the subsequence sum
# is as high as possible and the subsequence's elements are in increasing order.


# Recursive Approach
def max_sum_inc_subsequece(a, index =0, prev=float("-inf"), suma=0):

    if index ==len(a):
        return suma
    
    max_sum = suma
    for i in range(index, len(a)):
        if a[i] > prev:
            max_sum_recursive = max_sum_inc_subsequece(a, i, a[i], suma + a[i])
            max_sum = max(max_sum_recursive, max_sum)

    return max_sum

# Recursive Solution - Alternative approach
def max_sum_inc_subseq_alt(a, index=0, prev=float("-inf")):
    if index == len(a):
        return 0
    
    from_next_element = max_sum_inc_subseq_alt(a, index+1, prev)
    from_current_element = 0

    if a[index] > prev:
        from_current_element = max_sum_inc_subseq_alt(a, index + 1, a[index]) + a[index]

    return max(from_current_element, from_next_element)

# Dynamic Programmming Approach
# Time: O(N**2)
# Space: O(N)

def max_sum_inc_subseq_dp(a):

    if not a :
        return 0
    
    DP = [0]*len(a)
    DP[0] = a[0]

    for i in range(1, len(a)):
        for j in range(i):

            if a[j] < a[i] and DP[j] > DP[i]:
                DP[i] = DP[j]
        
        DP[i] = DP[i] + a[i]

    return max(DP)

if __name__ == "__main__":

    a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
    max_sum_inc_subseq_dp(a)
    max_sum_inc_subsequece(a)
    max_sum_inc_subseq_alt(a)

    