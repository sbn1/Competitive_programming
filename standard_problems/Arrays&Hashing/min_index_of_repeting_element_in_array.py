# Given an integer array, find the minimum index of a repeating element in linear
#  time and doing just a single traversal of the array.
# 
#Traverse the array from the tail, and save first appearence. If the element already saved 
# in the stack, save the postion. The last appearence of an element that already exist is the
# solution.

# Time: O(N)
# Space: O(N)

def findMinIndex(arr):
    # saves the last appearence of an already seen element
    min_index = len(arr)
    # empty set to store the elements
    stack = set()
    # traverse the array from right
    for i in range(len(arr)-1,-1,-1):
        # if the element is seen for first time, it is stored
        if arr[i] not in stack:
            stack.add(arr[i])
        else:
            # if the element is seen before, store the position
            min_index = i
    # if there are no repeating elements return -1
    if min_index == len(arr):
        return -1
    return min_index



if __name__ == "__main__":

    findMinIndex([5, 6, 3, 4, 3, 6, 4])
