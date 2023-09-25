#Given a sorted integer array, find a pair in it having an absolute minimum sum.

#Use Two Pinters and check if the abs sum is lower than minimun, if yes, update the minimum and indexes, 
# move toward the center.

# Time: O(N)
# Space: O(1)
def findPair(arr):

    # check base case
    if len(arr) < 2:
        return 
    # initiate the left and right pointers 
    l, r = 0, len(arr)-1
    # initiate the positions of the elements that store the positions
    pozition_nr_1  = pozition_nr_2 = 0
    # initiate the minimum that will be updated
    min_abs_sum = float("inf")
    while l < r:
        absolute_sum = abs(arr[l] + arr[r])
        # update the minimum in case that there is a lower value
        if  absolute_sum < min_abs_sum:
            min_abs_sum = absolute_sum
            # save the postions 
            pozition_nr_1, pozition_nr_2 = l, r
        # the optimal solution
        if min_abs_sum == 0:
            break 
        # if both are negative, move toward center from left
        if arr[l] + arr[r] < 0:
            l += 1
        else:
            # if both positive, also move toward center from right
            r -= 1
    
    return arr[pozition_nr_1], arr[pozition_nr_2]

if __name__ == "__main__":

    findPair([-6, -5, -3, 0, 2, 4, 9])
