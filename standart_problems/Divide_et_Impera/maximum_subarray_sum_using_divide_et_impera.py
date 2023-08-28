# Given an integer array, find the maximum sum among all subarrays possible.
# Divide the array in two equal subarrays, fid the max subarray from the left side 
# and from the right side. Find the maximum subarray sum that crosses the middle element.
# Take the maximum of all the three sums.

# Time: O(N*Log(N))
#Space: O(Log N)

def compute_maximum_sum_left_right(a, mid):

    left_side = right_side = float("-inf")
    suma = 0
    for i in range(mid-1, -1, -1):
        suma += a[i]
        left_side = max(left_side, suma)
    suma = 0
    for i in range(mid, len(a)):
        suma += a[i]
        right_side = max(right_side, suma)
    
    return left_side + right_side

def find_max_subarray_sum(a):
    if len(a) ==1:
        return a[0]
    if not a:
        return 0
    
    mid = len(a)//2

    left_side = find_max_subarray_sum(a[:mid])
    right_side = find_max_subarray_sum(a[mid:])

    both_sides = compute_maximum_sum_left_right(a, mid)

    return max(left_side, right_side, both_sides)

if __name__ == "__main__":

    find_max_subarray_sum([2, -4, 1, 9, -6, 7, -3])





    