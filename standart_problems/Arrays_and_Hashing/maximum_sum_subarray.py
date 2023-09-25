# Given an integer array, find a continuous subarray withn it 
# that has the largest sum
# Kadane's Algorithms
# 
# create on variable that will store the max sublist up to this point, 
# and one variable that will store the max sum of sublist ending at the 
# current position
# Time: O(N)
# Space: O(1)

def kadane(arr):
    # stores the maximum sublist found up to this point
    max_so_far = 0
    # stores the maximum sum of sublists ending at the current position
    max_ending_here = 0

    for i in arr:
        max_ending_here = max(max_ending_here+i, i, 0)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

if __name__ == "__main__":

    kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    kadane([5, 4, -1, 7, 8])
    kadane([1])